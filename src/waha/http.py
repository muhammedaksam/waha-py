from typing import Any, Optional

import httpx


class WahaHttpClient:
    """HTTP client wrapper providing sync and async request methods using httpx."""

    def __init__(
        self,
        base_url: str,
        api_key: Optional[str] = None,
        headers: Optional[dict[str, str]] = None,
        timeout: float = 60.0,
        client: Optional[httpx.Client] = None,
        async_client: Optional[httpx.AsyncClient] = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout

        req_headers = {"Accept": "application/json"}
        if api_key:
            req_headers["X-Api-Key"] = api_key
        if headers:
            req_headers.update(headers)

        self._sync_client = client or httpx.Client(
            base_url=self.base_url,
            headers=req_headers,
            timeout=self.timeout,
        )
        self._async_client = async_client or httpx.AsyncClient(
            base_url=self.base_url,
            headers=req_headers,
            timeout=self.timeout,
        )

    def request(
        self,
        method: str,
        path: str,
        params: Optional[dict[str, Any]] = None,
        json: Optional[Any] = None,
        headers: Optional[dict[str, str]] = None,
        files: Optional[Any] = None,
        data: Optional[Any] = None,
    ) -> httpx.Response:
        """Perform a synchronous HTTP request."""
        # Filter out None query parameters
        clean_params = {k: v for k, v in params.items() if v is not None} if params else None

        response = self._sync_client.request(
            method=method,
            url=path,
            params=clean_params,
            json=json,
            headers=headers,
            files=files,
            data=data,
        )
        response.raise_for_status()
        return response

    async def arequest(
        self,
        method: str,
        path: str,
        params: Optional[dict[str, Any]] = None,
        json: Optional[Any] = None,
        headers: Optional[dict[str, str]] = None,
        files: Optional[Any] = None,
        data: Optional[Any] = None,
    ) -> httpx.Response:
        """Perform an asynchronous HTTP request."""
        clean_params = {k: v for k, v in params.items() if v is not None} if params else None

        response = await self._async_client.request(
            method=method,
            url=path,
            params=clean_params,
            json=json,
            headers=headers,
            files=files,
            data=data,
        )
        response.raise_for_status()
        return response

    def close(self) -> None:
        """Close the underlying sync and async HTTP clients."""
        self._sync_client.close()

    async def aclose(self) -> None:
        """Close the underlying async HTTP client."""
        await self._async_client.aclose()
        self._sync_client.close()
