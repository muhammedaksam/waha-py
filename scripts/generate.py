#!/usr/bin/env python3
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
OPENAPI_PATH = ROOT_DIR / "openapi.json"
CLEANED_OPENAPI_PATH = ROOT_DIR / "openapi_cleaned.json"
MODELS_PATH = ROOT_DIR / "src" / "waha" / "generated" / "models.py"
API_PATH = ROOT_DIR / "src" / "waha" / "generated" / "api.py"
CLIENT_PATH = ROOT_DIR / "src" / "waha" / "client.py"


def sanitize_openapi(node, parent=None, prop_name=None):
    if isinstance(node, dict):
        if "required" in node and isinstance(node["required"], bool):
            is_req = node["required"]
            del node["required"]
            if is_req and parent is not None and prop_name is not None and isinstance(parent, dict):
                reqs = parent.get("required")
                if not isinstance(reqs, list):
                    reqs = []
                    parent["required"] = reqs
                if prop_name not in reqs:
                    reqs.append(prop_name)

        if "properties" in node and isinstance(node["properties"], dict):
            for k, v in list(node["properties"].items()):
                sanitize_openapi(v, parent=node, prop_name=k)

        for k, v in list(node.items()):
            if k != "properties":
                sanitize_openapi(v, parent=node, prop_name=k)

    elif isinstance(node, list):
        for item in node:
            sanitize_openapi(item)


def camel_to_snake(name: str) -> str:
    # Handle acronyms and camelCase conversion
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    name = re.sub(r"[^a-zA-Z0-9_]", "_", name)
    return name.lower()


def clean_controller_name(name: str) -> str:
    name = re.sub(r"Controller$", "", name)
    name = re.sub(r"[^a-zA-Z0-9]", "", name)
    return name


def main():
    print("1. Sanitizing OpenAPI specification...")
    with open(OPENAPI_PATH) as f:
        spec = json.load(f)

    sanitize_openapi(spec)

    with open(CLEANED_OPENAPI_PATH, "w") as f:
        json.dump(spec, f, indent=2)

    MODELS_PATH.parent.mkdir(parents=True, exist_ok=True)

    print("2. Generating Pydantic models with datamodel-code-generator...")
    cmd = [
        sys.executable,
        "-m",
        "datamodel_code_generator",
        "--input",
        str(CLEANED_OPENAPI_PATH),
        "--input-file-type",
        "openapi",
        "--output",
        str(MODELS_PATH),
        "--output-model-type",
        "pydantic_v2.BaseModel",
        "--target-python-version",
        "3.10",
    ]
    subprocess.run(cmd, check=True)

    print("3. Generating API Controllers...")
    paths = spec.get("paths", {})
    controllers: dict[str, list[dict]] = {}

    for path_str, methods in paths.items():
        for method_name, op in methods.items():
            if not isinstance(op, dict):
                continue
            op_id = op.get("operationId", "")
            if "_" in op_id:
                raw_ctrl, raw_method = op_id.split("_", 1)
            else:
                tags = op.get("tags", ["Default"])
                raw_ctrl = tags[0] if tags else "Default"
                raw_method = op_id or method_name

            ctrl_key = clean_controller_name(raw_ctrl)
            if not ctrl_key:
                ctrl_key = "Default"

            if ctrl_key not in controllers:
                controllers[ctrl_key] = []

            # Extract params
            path_params = []
            query_params = []
            for p in op.get("parameters", []):
                if p.get("in") == "path":
                    path_params.append(p.get("name"))
                elif p.get("in") == "query":
                    query_params.append(p.get("name"))

            has_body = "requestBody" in op

            controllers[ctrl_key].append(
                {
                    "op_id": op_id,
                    "raw_method": raw_method,
                    "method_name": camel_to_snake(raw_method),
                    "http_method": method_name.upper(),
                    "path": path_str,
                    "summary": op.get("summary", ""),
                    "path_params": path_params,
                    "query_params": query_params,
                    "has_body": has_body,
                }
            )

    api_code = [
        "from typing import Any, Optional, Union",
        "from ..http import WahaHttpClient",
        "",
    ]

    controller_classes = []

    for ctrl_name, ops in controllers.items():
        class_name = f"{ctrl_name}Api"
        controller_classes.append((ctrl_name, class_name))

        api_code.append(f"class {class_name}:")
        api_code.append(f'    """API Controller for {ctrl_name}."""')
        api_code.append("")
        api_code.append("    def __init__(self, http_client: WahaHttpClient) -> None:")
        api_code.append("        self._http = http_client")
        api_code.append("")

        seen_methods: set[str] = set()

        for op in ops:
            m_name = op["method_name"]
            if m_name in seen_methods:
                m_name = f"{m_name}_{op['http_method'].lower()}"
            seen_methods.add(m_name)

            path_args = op["path_params"]
            has_body = op["has_body"]
            query_args = op["query_params"]

            # Method signature
            sig_args = ["self"]
            for pa in path_args:
                sig_args.append(f"{camel_to_snake(pa)}: str")
            if has_body:
                sig_args.append("payload: Optional[Union[dict[str, Any], Any]] = None")
            if query_args:
                sig_args.append("params: Optional[dict[str, Any]] = None")
            sig_args.append("**kwargs: Any")

            sig_str = ", ".join(sig_args)

            doc = op["summary"].replace('"', '\\"') if op["summary"] else f"{op['http_method']} {op['path']}"

            # Path formatting string
            formatted_path = op["path"]
            for pa in path_args:
                formatted_path = formatted_path.replace("{" + pa + "}", "{" + camel_to_snake(pa) + "}")

            # Sync method
            api_code.append(f"    def {m_name}({sig_str}) -> Any:")
            api_code.append(f'        """{doc}"""')
            api_code.append(f'        url = f"{formatted_path}"')
            api_code.append("        request_kwargs = {}")
            if has_body:
                api_code.append("        if payload is not None:")
                api_code.append(
                    "            request_kwargs['json'] = payload if isinstance(payload, dict) else (payload.model_dump() if hasattr(payload, 'model_dump') else payload)"
                )
            if query_args:
                api_code.append("        if params is not None:")
                api_code.append("            request_kwargs['params'] = params")
            api_code.append("        request_kwargs.update(kwargs)")
            api_code.append(f'        response = self._http.request("{op["http_method"]}", url, **request_kwargs)')
            api_code.append("        try:")
            api_code.append("            return response.json()")
            api_code.append("        except Exception:")
            api_code.append("            return response.text")
            api_code.append("")

            # Async method
            api_code.append(f"    async def a_{m_name}({sig_str}) -> Any:")
            api_code.append(f'        """{doc} (async)"""')
            api_code.append(f'        url = f"{formatted_path}"')
            api_code.append("        request_kwargs = {}")
            if has_body:
                api_code.append("        if payload is not None:")
                api_code.append(
                    "            request_kwargs['json'] = payload if isinstance(payload, dict) else (payload.model_dump() if hasattr(payload, 'model_dump') else payload)"
                )
            if query_args:
                api_code.append("        if params is not None:")
                api_code.append("            request_kwargs['params'] = params")
            api_code.append("        request_kwargs.update(kwargs)")
            api_code.append(
                f'        response = await self._http.arequest("{op["http_method"]}", url, **request_kwargs)'
            )
            api_code.append("        try:")
            api_code.append("            return response.json()")
            api_code.append("        except Exception:")
            api_code.append("            return response.text")
            api_code.append("")

    API_PATH.write_text("\n".join(api_code))
    print(f"Wrote API Controllers to {API_PATH}")

    print("4. Generating WahaClient and AsyncWahaClient...")
    client_code = [
        "from typing import Optional",
        "import httpx",
        "from .http import WahaHttpClient",
        "from .generated.api import (",
    ]
    for ctrl_name, class_name in controller_classes:
        client_code.append(f"    {class_name},")
    client_code.append(")")
    client_code.append("")
    client_code.append("class WahaClient:")
    client_code.append('    """Synchronous WAHA Client providing access to all API controllers."""')
    client_code.append("")
    client_code.append("    def __init__(")
    client_code.append("        self,")
    client_code.append("        base_url: str,")
    client_code.append("        api_key: Optional[str] = None,")
    client_code.append("        headers: Optional[dict[str, str]] = None,")
    client_code.append("        timeout: float = 60.0,")
    client_code.append("        http_client: Optional[WahaHttpClient] = None,")
    client_code.append("    ) -> None:")
    client_code.append("        self._http = http_client or WahaHttpClient(")
    client_code.append("            base_url=base_url, api_key=api_key, headers=headers, timeout=timeout")
    client_code.append("        )")
    client_code.append("")

    for ctrl_name, class_name in controller_classes:
        prop_name = camel_to_snake(ctrl_name)
        client_code.append(f"        self.{prop_name} = {class_name}(self._http)")

    client_code.append("")
    client_code.append("    def close(self) -> None:")
    client_code.append("        self._http.close()")
    client_code.append("")

    client_code.append("class AsyncWahaClient:")
    client_code.append('    """Asynchronous WAHA Client providing access to all API controllers."""')
    client_code.append("")
    client_code.append("    def __init__(")
    client_code.append("        self,")
    client_code.append("        base_url: str,")
    client_code.append("        api_key: Optional[str] = None,")
    client_code.append("        headers: Optional[dict[str, str]] = None,")
    client_code.append("        timeout: float = 60.0,")
    client_code.append("        http_client: Optional[WahaHttpClient] = None,")
    client_code.append("    ) -> None:")
    client_code.append("        self._http = http_client or WahaHttpClient(")
    client_code.append("            base_url=base_url, api_key=api_key, headers=headers, timeout=timeout")
    client_code.append("        )")
    client_code.append("")

    for ctrl_name, class_name in controller_classes:
        prop_name = camel_to_snake(ctrl_name)
        client_code.append(f"        self.{prop_name} = {class_name}(self._http)")

    client_code.append("")
    client_code.append("    async def close(self) -> None:")
    client_code.append("        await self._http.aclose()")
    client_code.append("")

    CLIENT_PATH.write_text("\n".join(client_code))
    print(f"Wrote WahaClient to {CLIENT_PATH}")

    print("5. Formatting code with ruff...")
    subprocess.run([sys.executable, "-m", "ruff", "check", "--fix", str(ROOT_DIR)], check=False)
    subprocess.run([sys.executable, "-m", "ruff", "format", str(ROOT_DIR)], check=False)

    print("Done!")


if __name__ == "__main__":
    main()
