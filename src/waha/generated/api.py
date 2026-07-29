from typing import Any, Optional, Union

from ..http import WahaHttpClient


class AuthApi:
    """API Controller for Auth."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def get_qr(self, session: str, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get QR code for pairing WhatsApp API."""
        url = f"/api/{session}/auth/qr"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_qr(self, session: str, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get QR code for pairing WhatsApp API. (async)"""
        url = f"/api/{session}/auth/qr"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def request_code(self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Request authentication code."""
        url = f"/api/{session}/auth/request-code"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_request_code(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Request authentication code. (async)"""
        url = f"/api/{session}/auth/request-code"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_passkey_challenge(self, session: str, **kwargs: Any) -> Any:
        """Get the pending passkey (WebAuthn) challenge."""
        url = f"/api/{session}/auth/passkey/challenge"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_passkey_challenge(self, session: str, **kwargs: Any) -> Any:
        """Get the pending passkey (WebAuthn) challenge. (async)"""
        url = f"/api/{session}/auth/passkey/challenge"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def submit_passkey(self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Submit a WebAuthn passkey assertion to finish pairing."""
        url = f"/api/{session}/auth/passkey"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_submit_passkey(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Submit a WebAuthn passkey assertion to finish pairing. (async)"""
        url = f"/api/{session}/auth/passkey"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_passkey_confirmation(self, session: str, **kwargs: Any) -> Any:
        """Get the pending passkey confirmation code."""
        url = f"/api/{session}/auth/passkey/confirmation"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_passkey_confirmation(self, session: str, **kwargs: Any) -> Any:
        """Get the pending passkey confirmation code. (async)"""
        url = f"/api/{session}/auth/passkey/confirmation"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def confirm_passkey(self, session: str, **kwargs: Any) -> Any:
        """Confirm passkey pairing (only needed for the manual code case)."""
        url = f"/api/{session}/auth/passkey/confirm"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_confirm_passkey(self, session: str, **kwargs: Any) -> Any:
        """Confirm passkey pairing (only needed for the manual code case). (async)"""
        url = f"/api/{session}/auth/passkey/confirm"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class ApiKeysApi:
    """API Controller for ApiKeys."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def create(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Create a new API key"""
        url = "/api/keys"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_create(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Create a new API key (async)"""
        url = "/api/keys"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def list(self, **kwargs: Any) -> Any:
        """Get all API keys"""
        url = "/api/keys"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_list(self, **kwargs: Any) -> Any:
        """Get all API keys (async)"""
        url = "/api/keys"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def media(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Create or get a media-download-only API key for a session"""
        url = "/api/keys/media"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_media(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Create or get a media-download-only API key for a session (async)"""
        url = "/api/keys/media"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def control(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Create or get a control-only API key for a session"""
        url = "/api/keys/control"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_control(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Create or get a control-only API key for a session (async)"""
        url = "/api/keys/control"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def update(self, id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Update an API key"""
        url = f"/api/keys/{id}"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_update(self, id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Update an API key (async)"""
        url = f"/api/keys/{id}"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def delete(self, id: str, **kwargs: Any) -> Any:
        """Delete an API key"""
        url = f"/api/keys/{id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("DELETE", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_delete(self, id: str, **kwargs: Any) -> Any:
        """Delete an API key (async)"""
        url = f"/api/keys/{id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("DELETE", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class SessionsApi:
    """API Controller for Sessions."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def list(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """List all sessions"""
        url = "/api/sessions"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_list(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """List all sessions (async)"""
        url = "/api/sessions"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def create(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Create a session"""
        url = "/api/sessions"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_create(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Create a session (async)"""
        url = "/api/sessions"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get(self, session: str, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get session information"""
        url = f"/api/sessions/{session}"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get(self, session: str, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get session information (async)"""
        url = f"/api/sessions/{session}"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def update(self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Update a session"""
        url = f"/api/sessions/{session}"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_update(self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Update a session (async)"""
        url = f"/api/sessions/{session}"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def delete(self, session: str, **kwargs: Any) -> Any:
        """Delete the session"""
        url = f"/api/sessions/{session}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("DELETE", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_delete(self, session: str, **kwargs: Any) -> Any:
        """Delete the session (async)"""
        url = f"/api/sessions/{session}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("DELETE", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_me(self, session: str, **kwargs: Any) -> Any:
        """Get information about the authenticated account"""
        url = f"/api/sessions/{session}/me"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_me(self, session: str, **kwargs: Any) -> Any:
        """Get information about the authenticated account (async)"""
        url = f"/api/sessions/{session}/me"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def start(self, session: str, **kwargs: Any) -> Any:
        """Start the session"""
        url = f"/api/sessions/{session}/start"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_start(self, session: str, **kwargs: Any) -> Any:
        """Start the session (async)"""
        url = f"/api/sessions/{session}/start"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def stop(self, session: str, **kwargs: Any) -> Any:
        """Stop the session"""
        url = f"/api/sessions/{session}/stop"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_stop(self, session: str, **kwargs: Any) -> Any:
        """Stop the session (async)"""
        url = f"/api/sessions/{session}/stop"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def logout(self, session: str, **kwargs: Any) -> Any:
        """Logout from the session"""
        url = f"/api/sessions/{session}/logout"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_logout(self, session: str, **kwargs: Any) -> Any:
        """Logout from the session (async)"""
        url = f"/api/sessions/{session}/logout"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def restart(self, session: str, **kwargs: Any) -> Any:
        """Restart the session"""
        url = f"/api/sessions/{session}/restart"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_restart(self, session: str, **kwargs: Any) -> Any:
        """Restart the session (async)"""
        url = f"/api/sessions/{session}/restart"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def depracated_start(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Upsert and Start session"""
        url = "/api/sessions/start"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_depracated_start(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Upsert and Start session (async)"""
        url = "/api/sessions/start"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def deprecated_stop(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Stop (and Logout if asked) session"""
        url = "/api/sessions/stop"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_deprecated_stop(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Stop (and Logout if asked) session (async)"""
        url = "/api/sessions/stop"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def deprecated_logout(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Logout and Delete session."""
        url = "/api/sessions/logout"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_deprecated_logout(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Logout and Delete session. (async)"""
        url = "/api/sessions/logout"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class ProfileApi:
    """API Controller for Profile."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def get_my_profile(self, session: str, **kwargs: Any) -> Any:
        """Get my profile"""
        url = f"/api/{session}/profile"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_my_profile(self, session: str, **kwargs: Any) -> Any:
        """Get my profile (async)"""
        url = f"/api/{session}/profile"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def set_profile_name(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Set my profile name"""
        url = f"/api/{session}/profile/name"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_set_profile_name(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Set my profile name (async)"""
        url = f"/api/{session}/profile/name"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def set_profile_status(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Set profile status (About)"""
        url = f"/api/{session}/profile/status"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_set_profile_status(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Set profile status (About) (async)"""
        url = f"/api/{session}/profile/status"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def set_profile_picture(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Set profile picture"""
        url = f"/api/{session}/profile/picture"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_set_profile_picture(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Set profile picture (async)"""
        url = f"/api/{session}/profile/picture"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def delete_profile_picture(self, session: str, **kwargs: Any) -> Any:
        """Delete profile picture"""
        url = f"/api/{session}/profile/picture"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("DELETE", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_delete_profile_picture(self, session: str, **kwargs: Any) -> Any:
        """Delete profile picture (async)"""
        url = f"/api/{session}/profile/picture"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("DELETE", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class ChattingApi:
    """API Controller for Chatting."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def send_text(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Send a text message"""
        url = "/api/sendText"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_send_text(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Send a text message (async)"""
        url = "/api/sendText"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def send_text_get(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Send a text message"""
        url = "/api/sendText"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_send_text_get(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Send a text message (async)"""
        url = "/api/sendText"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def send_image(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Send an image"""
        url = "/api/sendImage"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_send_image(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Send an image (async)"""
        url = "/api/sendImage"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def send_file(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Send a file"""
        url = "/api/sendFile"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_send_file(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Send a file (async)"""
        url = "/api/sendFile"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def send_voice(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Send an voice message"""
        url = "/api/sendVoice"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_send_voice(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Send an voice message (async)"""
        url = "/api/sendVoice"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def send_video(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Send a video"""
        url = "/api/sendVideo"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_send_video(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Send a video (async)"""
        url = "/api/sendVideo"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def send_link_custom_preview(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Send a text message with a CUSTOM link preview."""
        url = "/api/send/link-custom-preview"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_send_link_custom_preview(
        self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Send a text message with a CUSTOM link preview. (async)"""
        url = "/api/send/link-custom-preview"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def send_buttons(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Send buttons message (interactive)"""
        url = "/api/sendButtons"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_send_buttons(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Send buttons message (interactive) (async)"""
        url = "/api/sendButtons"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def send_list(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Send a list message (interactive)"""
        url = "/api/sendList"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_send_list(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Send a list message (interactive) (async)"""
        url = "/api/sendList"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def forward_message(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """POST /api/forwardMessage"""
        url = "/api/forwardMessage"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_forward_message(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """POST /api/forwardMessage (async)"""
        url = "/api/forwardMessage"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def send_seen(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """POST /api/sendSeen"""
        url = "/api/sendSeen"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_send_seen(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """POST /api/sendSeen (async)"""
        url = "/api/sendSeen"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def start_typing(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """POST /api/startTyping"""
        url = "/api/startTyping"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_start_typing(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """POST /api/startTyping (async)"""
        url = "/api/startTyping"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def stop_typing(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """POST /api/stopTyping"""
        url = "/api/stopTyping"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_stop_typing(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """POST /api/stopTyping (async)"""
        url = "/api/stopTyping"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def set_reaction(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """React to a message with an emoji"""
        url = "/api/reaction"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_set_reaction(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """React to a message with an emoji (async)"""
        url = "/api/reaction"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def set_star(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Star or unstar a message"""
        url = "/api/star"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_set_star(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Star or unstar a message (async)"""
        url = "/api/star"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def send_poll(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Send a poll with options"""
        url = "/api/sendPoll"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_send_poll(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Send a poll with options (async)"""
        url = "/api/sendPoll"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def send_poll_vote(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Vote on a poll"""
        url = "/api/sendPollVote"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_send_poll_vote(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Vote on a poll (async)"""
        url = "/api/sendPollVote"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def send_location(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """POST /api/sendLocation"""
        url = "/api/sendLocation"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_send_location(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """POST /api/sendLocation (async)"""
        url = "/api/sendLocation"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def send_contact_vcard(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """POST /api/sendContactVcard"""
        url = "/api/sendContactVcard"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_send_contact_vcard(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """POST /api/sendContactVcard (async)"""
        url = "/api/sendContactVcard"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def send_buttons_reply(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Reply on a button message"""
        url = "/api/send/buttons/reply"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_send_buttons_reply(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Reply on a button message (async)"""
        url = "/api/send/buttons/reply"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_messages(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get messages in a chat"""
        url = "/api/messages"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_messages(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get messages in a chat (async)"""
        url = "/api/messages"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def deprecated_check_number_status(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Check number status"""
        url = "/api/checkNumberStatus"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_deprecated_check_number_status(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Check number status (async)"""
        url = "/api/checkNumberStatus"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def reply(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """DEPRECATED - you can set \"reply_to\" field when sending text, image, etc"""
        url = "/api/reply"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_reply(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """DEPRECATED - you can set \"reply_to\" field when sending text, image, etc (async)"""
        url = "/api/reply"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def send_link_preview_deprecated(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """POST /api/sendLinkPreview"""
        url = "/api/sendLinkPreview"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_send_link_preview_deprecated(
        self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """POST /api/sendLinkPreview (async)"""
        url = "/api/sendLinkPreview"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_new_message_id(self, session: str, **kwargs: Any) -> Any:
        """Generate a new message ID"""
        url = f"/api/{session}/new-message-id"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_new_message_id(self, session: str, **kwargs: Any) -> Any:
        """Generate a new message ID (async)"""
        url = f"/api/{session}/new-message-id"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class ChatsApi:
    """API Controller for Chats."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def get_chats(self, session: str, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get chats"""
        url = f"/api/{session}/chats"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_chats(self, session: str, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get chats (async)"""
        url = f"/api/{session}/chats"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_chats_overview(self, session: str, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get chats overview. Includes all necessary things to build UI \"your chats overview\" page - chat id, name, picture, last message. Sorting by last message timestamp"""
        url = f"/api/{session}/chats/overview"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_chats_overview(self, session: str, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get chats overview. Includes all necessary things to build UI \"your chats overview\" page - chat id, name, picture, last message. Sorting by last message timestamp (async)"""
        url = f"/api/{session}/chats/overview"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def post_chats_overview(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Get chats overview. Use POST if you have too many \"ids\" params - GET can limit it"""
        url = f"/api/{session}/chats/overview"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_post_chats_overview(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Get chats overview. Use POST if you have too many \"ids\" params - GET can limit it (async)"""
        url = f"/api/{session}/chats/overview"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def delete_chat(self, session: str, chat_id: str, **kwargs: Any) -> Any:
        """Deletes the chat"""
        url = f"/api/{session}/chats/{chat_id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("DELETE", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_delete_chat(self, session: str, chat_id: str, **kwargs: Any) -> Any:
        """Deletes the chat (async)"""
        url = f"/api/{session}/chats/{chat_id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("DELETE", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_chat_picture(
        self, session: str, chat_id: str, params: Optional[dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        """Gets chat picture"""
        url = f"/api/{session}/chats/{chat_id}/picture"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_chat_picture(
        self, session: str, chat_id: str, params: Optional[dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        """Gets chat picture (async)"""
        url = f"/api/{session}/chats/{chat_id}/picture"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_chat_messages(
        self, session: str, chat_id: str, params: Optional[dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        """Gets messages in the chat"""
        url = f"/api/{session}/chats/{chat_id}/messages"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_chat_messages(
        self, session: str, chat_id: str, params: Optional[dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        """Gets messages in the chat (async)"""
        url = f"/api/{session}/chats/{chat_id}/messages"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def clear_messages(self, session: str, chat_id: str, **kwargs: Any) -> Any:
        """Clears all messages from the chat"""
        url = f"/api/{session}/chats/{chat_id}/messages"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("DELETE", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_clear_messages(self, session: str, chat_id: str, **kwargs: Any) -> Any:
        """Clears all messages from the chat (async)"""
        url = f"/api/{session}/chats/{chat_id}/messages"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("DELETE", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def read_chat_messages(
        self, session: str, chat_id: str, params: Optional[dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        """Read unread messages in the chat"""
        url = f"/api/{session}/chats/{chat_id}/messages/read"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_read_chat_messages(
        self, session: str, chat_id: str, params: Optional[dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        """Read unread messages in the chat (async)"""
        url = f"/api/{session}/chats/{chat_id}/messages/read"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_chat_message(
        self, session: str, chat_id: str, message_id: str, params: Optional[dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        """Gets message by id"""
        url = f"/api/{session}/chats/{chat_id}/messages/{message_id}"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_chat_message(
        self, session: str, chat_id: str, message_id: str, params: Optional[dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        """Gets message by id (async)"""
        url = f"/api/{session}/chats/{chat_id}/messages/{message_id}"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def delete_message(self, session: str, chat_id: str, message_id: str, **kwargs: Any) -> Any:
        """Deletes a message from the chat"""
        url = f"/api/{session}/chats/{chat_id}/messages/{message_id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("DELETE", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_delete_message(self, session: str, chat_id: str, message_id: str, **kwargs: Any) -> Any:
        """Deletes a message from the chat (async)"""
        url = f"/api/{session}/chats/{chat_id}/messages/{message_id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("DELETE", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def edit_message(
        self,
        session: str,
        chat_id: str,
        message_id: str,
        payload: Optional[Union[dict[str, Any], Any]] = None,
        **kwargs: Any,
    ) -> Any:
        """Edits a message in the chat"""
        url = f"/api/{session}/chats/{chat_id}/messages/{message_id}"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_edit_message(
        self,
        session: str,
        chat_id: str,
        message_id: str,
        payload: Optional[Union[dict[str, Any], Any]] = None,
        **kwargs: Any,
    ) -> Any:
        """Edits a message in the chat (async)"""
        url = f"/api/{session}/chats/{chat_id}/messages/{message_id}"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def pin_message(
        self,
        session: str,
        chat_id: str,
        message_id: str,
        payload: Optional[Union[dict[str, Any], Any]] = None,
        **kwargs: Any,
    ) -> Any:
        """Pins a message in the chat"""
        url = f"/api/{session}/chats/{chat_id}/messages/{message_id}/pin"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_pin_message(
        self,
        session: str,
        chat_id: str,
        message_id: str,
        payload: Optional[Union[dict[str, Any], Any]] = None,
        **kwargs: Any,
    ) -> Any:
        """Pins a message in the chat (async)"""
        url = f"/api/{session}/chats/{chat_id}/messages/{message_id}/pin"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def unpin_message(self, session: str, chat_id: str, message_id: str, **kwargs: Any) -> Any:
        """Unpins a message in the chat"""
        url = f"/api/{session}/chats/{chat_id}/messages/{message_id}/unpin"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_unpin_message(self, session: str, chat_id: str, message_id: str, **kwargs: Any) -> Any:
        """Unpins a message in the chat (async)"""
        url = f"/api/{session}/chats/{chat_id}/messages/{message_id}/unpin"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def archive_chat(self, session: str, chat_id: str, **kwargs: Any) -> Any:
        """Archive the chat"""
        url = f"/api/{session}/chats/{chat_id}/archive"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_archive_chat(self, session: str, chat_id: str, **kwargs: Any) -> Any:
        """Archive the chat (async)"""
        url = f"/api/{session}/chats/{chat_id}/archive"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def unarchive_chat(self, session: str, chat_id: str, **kwargs: Any) -> Any:
        """Unarchive the chat"""
        url = f"/api/{session}/chats/{chat_id}/unarchive"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_unarchive_chat(self, session: str, chat_id: str, **kwargs: Any) -> Any:
        """Unarchive the chat (async)"""
        url = f"/api/{session}/chats/{chat_id}/unarchive"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def unread_chat(self, session: str, chat_id: str, **kwargs: Any) -> Any:
        """Unread the chat"""
        url = f"/api/{session}/chats/{chat_id}/unread"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_unread_chat(self, session: str, chat_id: str, **kwargs: Any) -> Any:
        """Unread the chat (async)"""
        url = f"/api/{session}/chats/{chat_id}/unread"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class CallsApi:
    """API Controller for Calls."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def reject_call(self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Reject incoming call"""
        url = f"/api/{session}/calls/reject"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_reject_call(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Reject incoming call (async)"""
        url = f"/api/{session}/calls/reject"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class ChannelsApi:
    """API Controller for Channels."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def list(self, session: str, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get list of know channels"""
        url = f"/api/{session}/channels"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_list(self, session: str, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get list of know channels (async)"""
        url = f"/api/{session}/channels"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def create(self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Create a new channel."""
        url = f"/api/{session}/channels"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_create(self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Create a new channel. (async)"""
        url = f"/api/{session}/channels"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def delete(self, session: str, id: str, **kwargs: Any) -> Any:
        """Delete the channel."""
        url = f"/api/{session}/channels/{id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("DELETE", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_delete(self, session: str, id: str, **kwargs: Any) -> Any:
        """Delete the channel. (async)"""
        url = f"/api/{session}/channels/{id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("DELETE", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get(self, session: str, id: str, **kwargs: Any) -> Any:
        """Get the channel info"""
        url = f"/api/{session}/channels/{id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get(self, session: str, id: str, **kwargs: Any) -> Any:
        """Get the channel info (async)"""
        url = f"/api/{session}/channels/{id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def preview_channel_messages(
        self, session: str, id: str, params: Optional[dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        """Preview channel messages"""
        url = f"/api/{session}/channels/{id}/messages/preview"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_preview_channel_messages(
        self, session: str, id: str, params: Optional[dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        """Preview channel messages (async)"""
        url = f"/api/{session}/channels/{id}/messages/preview"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def follow(self, session: str, id: str, **kwargs: Any) -> Any:
        """Follow the channel."""
        url = f"/api/{session}/channels/{id}/follow"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_follow(self, session: str, id: str, **kwargs: Any) -> Any:
        """Follow the channel. (async)"""
        url = f"/api/{session}/channels/{id}/follow"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def unfollow(self, session: str, id: str, **kwargs: Any) -> Any:
        """Unfollow the channel."""
        url = f"/api/{session}/channels/{id}/unfollow"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_unfollow(self, session: str, id: str, **kwargs: Any) -> Any:
        """Unfollow the channel. (async)"""
        url = f"/api/{session}/channels/{id}/unfollow"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def mute(self, session: str, id: str, **kwargs: Any) -> Any:
        """Mute the channel."""
        url = f"/api/{session}/channels/{id}/mute"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_mute(self, session: str, id: str, **kwargs: Any) -> Any:
        """Mute the channel. (async)"""
        url = f"/api/{session}/channels/{id}/mute"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def unmute(self, session: str, id: str, **kwargs: Any) -> Any:
        """Unmute the channel."""
        url = f"/api/{session}/channels/{id}/unmute"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_unmute(self, session: str, id: str, **kwargs: Any) -> Any:
        """Unmute the channel. (async)"""
        url = f"/api/{session}/channels/{id}/unmute"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def search_by_view(self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Search for channels (by view)"""
        url = f"/api/{session}/channels/search/by-view"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_search_by_view(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Search for channels (by view) (async)"""
        url = f"/api/{session}/channels/search/by-view"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def search_by_text(self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Search for channels (by text)"""
        url = f"/api/{session}/channels/search/by-text"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_search_by_text(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Search for channels (by text) (async)"""
        url = f"/api/{session}/channels/search/by-text"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_search_views(self, session: str, **kwargs: Any) -> Any:
        """Get list of views for channel search"""
        url = f"/api/{session}/channels/search/views"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_search_views(self, session: str, **kwargs: Any) -> Any:
        """Get list of views for channel search (async)"""
        url = f"/api/{session}/channels/search/views"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_search_countries(self, session: str, **kwargs: Any) -> Any:
        """Get list of countries for channel search"""
        url = f"/api/{session}/channels/search/countries"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_search_countries(self, session: str, **kwargs: Any) -> Any:
        """Get list of countries for channel search (async)"""
        url = f"/api/{session}/channels/search/countries"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_search_categories(self, session: str, **kwargs: Any) -> Any:
        """Get list of categories for channel search"""
        url = f"/api/{session}/channels/search/categories"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_search_categories(self, session: str, **kwargs: Any) -> Any:
        """Get list of categories for channel search (async)"""
        url = f"/api/{session}/channels/search/categories"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class StatusApi:
    """API Controller for Status."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def send_text_status(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Send text status"""
        url = f"/api/{session}/status/text"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_send_text_status(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Send text status (async)"""
        url = f"/api/{session}/status/text"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def send_image_status(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Send image status"""
        url = f"/api/{session}/status/image"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_send_image_status(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Send image status (async)"""
        url = f"/api/{session}/status/image"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def send_voice_status(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Send voice status"""
        url = f"/api/{session}/status/voice"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_send_voice_status(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Send voice status (async)"""
        url = f"/api/{session}/status/voice"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def send_video_status(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Send video status"""
        url = f"/api/{session}/status/video"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_send_video_status(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Send video status (async)"""
        url = f"/api/{session}/status/video"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def delete_status(self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """DELETE sent status"""
        url = f"/api/{session}/status/delete"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_delete_status(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """DELETE sent status (async)"""
        url = f"/api/{session}/status/delete"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_new_message_id(self, session: str, **kwargs: Any) -> Any:
        """Generate message ID you can use to batch contacts"""
        url = f"/api/{session}/status/new-message-id"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_new_message_id(self, session: str, **kwargs: Any) -> Any:
        """Generate message ID you can use to batch contacts (async)"""
        url = f"/api/{session}/status/new-message-id"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class LabelsApi:
    """API Controller for Labels."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def get_all(self, session: str, **kwargs: Any) -> Any:
        """Get all labels"""
        url = f"/api/{session}/labels"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_all(self, session: str, **kwargs: Any) -> Any:
        """Get all labels (async)"""
        url = f"/api/{session}/labels"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def create(self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Create a new label"""
        url = f"/api/{session}/labels"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_create(self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Create a new label (async)"""
        url = f"/api/{session}/labels"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def update(
        self, session: str, label_id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Update a label"""
        url = f"/api/{session}/labels/{label_id}"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_update(
        self, session: str, label_id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Update a label (async)"""
        url = f"/api/{session}/labels/{label_id}"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def delete(self, session: str, label_id: str, **kwargs: Any) -> Any:
        """Delete a label"""
        url = f"/api/{session}/labels/{label_id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("DELETE", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_delete(self, session: str, label_id: str, **kwargs: Any) -> Any:
        """Delete a label (async)"""
        url = f"/api/{session}/labels/{label_id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("DELETE", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_chat_labels(self, session: str, chat_id: str, **kwargs: Any) -> Any:
        """Get labels for the chat"""
        url = f"/api/{session}/labels/chats/{chat_id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_chat_labels(self, session: str, chat_id: str, **kwargs: Any) -> Any:
        """Get labels for the chat (async)"""
        url = f"/api/{session}/labels/chats/{chat_id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def put_chat_labels(
        self, session: str, chat_id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Save labels for the chat"""
        url = f"/api/{session}/labels/chats/{chat_id}"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_put_chat_labels(
        self, session: str, chat_id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Save labels for the chat (async)"""
        url = f"/api/{session}/labels/chats/{chat_id}"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_chats_by_label(self, session: str, label_id: str, **kwargs: Any) -> Any:
        """Get chats by label"""
        url = f"/api/{session}/labels/{label_id}/chats"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_chats_by_label(self, session: str, label_id: str, **kwargs: Any) -> Any:
        """Get chats by label (async)"""
        url = f"/api/{session}/labels/{label_id}/chats"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class ContactsApi:
    """API Controller for Contacts."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def get_all(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get all contacts"""
        url = "/api/contacts/all"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_all(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get all contacts (async)"""
        url = "/api/contacts/all"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get contact basic info"""
        url = "/api/contacts"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get contact basic info (async)"""
        url = "/api/contacts"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def check_exists(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Check phone number is registered in WhatsApp."""
        url = "/api/contacts/check-exists"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_check_exists(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Check phone number is registered in WhatsApp. (async)"""
        url = "/api/contacts/check-exists"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_about(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Gets the Contact's \"about\" info"""
        url = "/api/contacts/about"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_about(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Gets the Contact's \"about\" info (async)"""
        url = "/api/contacts/about"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_profile_picture(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get contact's profile picture URL"""
        url = "/api/contacts/profile-picture"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_profile_picture(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get contact's profile picture URL (async)"""
        url = "/api/contacts/profile-picture"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def block(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Block contact"""
        url = "/api/contacts/block"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_block(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Block contact (async)"""
        url = "/api/contacts/block"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def unblock(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Unblock contact"""
        url = "/api/contacts/unblock"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_unblock(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Unblock contact (async)"""
        url = "/api/contacts/unblock"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class ContactsSessionApi:
    """API Controller for ContactsSession."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def get(self, session: str, id: str, **kwargs: Any) -> Any:
        """Get contact basic info"""
        url = f"/api/{session}/contacts/{id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get(self, session: str, id: str, **kwargs: Any) -> Any:
        """Get contact basic info (async)"""
        url = f"/api/{session}/contacts/{id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def put(
        self, session: str, chat_id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Create or update contact"""
        url = f"/api/{session}/contacts/{chat_id}"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_put(
        self, session: str, chat_id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Create or update contact (async)"""
        url = f"/api/{session}/contacts/{chat_id}"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class LidsApi:
    """API Controller for Lids."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def get_all(self, session: str, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get all known lids to phone number mapping"""
        url = f"/api/{session}/lids"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_all(self, session: str, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get all known lids to phone number mapping (async)"""
        url = f"/api/{session}/lids"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_lids_count(self, session: str, **kwargs: Any) -> Any:
        """Get the number of known lids"""
        url = f"/api/{session}/lids/count"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_lids_count(self, session: str, **kwargs: Any) -> Any:
        """Get the number of known lids (async)"""
        url = f"/api/{session}/lids/count"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def find_pn_by_lid(self, session: str, lid: str, **kwargs: Any) -> Any:
        """Get phone number by lid"""
        url = f"/api/{session}/lids/{lid}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_find_pn_by_lid(self, session: str, lid: str, **kwargs: Any) -> Any:
        """Get phone number by lid (async)"""
        url = f"/api/{session}/lids/{lid}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def find_lid_by_phone_number(self, session: str, phone_number: str, **kwargs: Any) -> Any:
        """Get lid by phone number (chat id)"""
        url = f"/api/{session}/lids/pn/{phone_number}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_find_lid_by_phone_number(self, session: str, phone_number: str, **kwargs: Any) -> Any:
        """Get lid by phone number (chat id) (async)"""
        url = f"/api/{session}/lids/pn/{phone_number}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class GroupsApi:
    """API Controller for Groups."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def create_group(self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Create a new group."""
        url = f"/api/{session}/groups"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_create_group(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Create a new group. (async)"""
        url = f"/api/{session}/groups"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_groups(self, session: str, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get all groups."""
        url = f"/api/{session}/groups"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_groups(self, session: str, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get all groups. (async)"""
        url = f"/api/{session}/groups"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def join_info_group(self, session: str, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get info about the group before joining."""
        url = f"/api/{session}/groups/join-info"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_join_info_group(self, session: str, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get info about the group before joining. (async)"""
        url = f"/api/{session}/groups/join-info"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def join_group(self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Join group via code"""
        url = f"/api/{session}/groups/join"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_join_group(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Join group via code (async)"""
        url = f"/api/{session}/groups/join"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_groups_count(self, session: str, **kwargs: Any) -> Any:
        """Get the number of groups."""
        url = f"/api/{session}/groups/count"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_groups_count(self, session: str, **kwargs: Any) -> Any:
        """Get the number of groups. (async)"""
        url = f"/api/{session}/groups/count"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def refresh_groups(self, session: str, **kwargs: Any) -> Any:
        """Refresh groups from the server."""
        url = f"/api/{session}/groups/refresh"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_refresh_groups(self, session: str, **kwargs: Any) -> Any:
        """Refresh groups from the server. (async)"""
        url = f"/api/{session}/groups/refresh"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_group(self, session: str, id: str, **kwargs: Any) -> Any:
        """Get the group."""
        url = f"/api/{session}/groups/{id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_group(self, session: str, id: str, **kwargs: Any) -> Any:
        """Get the group. (async)"""
        url = f"/api/{session}/groups/{id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def delete_group(self, session: str, id: str, **kwargs: Any) -> Any:
        """Delete the group."""
        url = f"/api/{session}/groups/{id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("DELETE", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_delete_group(self, session: str, id: str, **kwargs: Any) -> Any:
        """Delete the group. (async)"""
        url = f"/api/{session}/groups/{id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("DELETE", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def leave_group(self, session: str, id: str, **kwargs: Any) -> Any:
        """Leave the group."""
        url = f"/api/{session}/groups/{id}/leave"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_leave_group(self, session: str, id: str, **kwargs: Any) -> Any:
        """Leave the group. (async)"""
        url = f"/api/{session}/groups/{id}/leave"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_chat_picture(self, session: str, id: str, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get group picture"""
        url = f"/api/{session}/groups/{id}/picture"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_chat_picture(
        self, session: str, id: str, params: Optional[dict[str, Any]] = None, **kwargs: Any
    ) -> Any:
        """Get group picture (async)"""
        url = f"/api/{session}/groups/{id}/picture"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def set_picture(
        self, id: str, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Set group picture"""
        url = f"/api/{session}/groups/{id}/picture"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_set_picture(
        self, id: str, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Set group picture (async)"""
        url = f"/api/{session}/groups/{id}/picture"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def delete_picture(self, id: str, session: str, **kwargs: Any) -> Any:
        """Delete group picture"""
        url = f"/api/{session}/groups/{id}/picture"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("DELETE", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_delete_picture(self, id: str, session: str, **kwargs: Any) -> Any:
        """Delete group picture (async)"""
        url = f"/api/{session}/groups/{id}/picture"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("DELETE", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def set_description(
        self, session: str, id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Updates the group description."""
        url = f"/api/{session}/groups/{id}/description"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_set_description(
        self, session: str, id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Updates the group description. (async)"""
        url = f"/api/{session}/groups/{id}/description"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def set_subject(
        self, session: str, id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Updates the group subject"""
        url = f"/api/{session}/groups/{id}/subject"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_set_subject(
        self, session: str, id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Updates the group subject (async)"""
        url = f"/api/{session}/groups/{id}/subject"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def set_info_admin_only(
        self, session: str, id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Updates the group \"info admin only\" settings."""
        url = f"/api/{session}/groups/{id}/settings/security/info-admin-only"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_set_info_admin_only(
        self, session: str, id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Updates the group \"info admin only\" settings. (async)"""
        url = f"/api/{session}/groups/{id}/settings/security/info-admin-only"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_info_admin_only(self, session: str, id: str, **kwargs: Any) -> Any:
        """Get the group's 'info admin only' settings."""
        url = f"/api/{session}/groups/{id}/settings/security/info-admin-only"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_info_admin_only(self, session: str, id: str, **kwargs: Any) -> Any:
        """Get the group's 'info admin only' settings. (async)"""
        url = f"/api/{session}/groups/{id}/settings/security/info-admin-only"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def set_messages_admin_only(
        self, session: str, id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Update settings - who can send messages"""
        url = f"/api/{session}/groups/{id}/settings/security/messages-admin-only"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_set_messages_admin_only(
        self, session: str, id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Update settings - who can send messages (async)"""
        url = f"/api/{session}/groups/{id}/settings/security/messages-admin-only"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_messages_admin_only(self, session: str, id: str, **kwargs: Any) -> Any:
        """Get settings - who can send messages"""
        url = f"/api/{session}/groups/{id}/settings/security/messages-admin-only"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_messages_admin_only(self, session: str, id: str, **kwargs: Any) -> Any:
        """Get settings - who can send messages (async)"""
        url = f"/api/{session}/groups/{id}/settings/security/messages-admin-only"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_invite_code(self, session: str, id: str, **kwargs: Any) -> Any:
        """Gets the invite code for the group."""
        url = f"/api/{session}/groups/{id}/invite-code"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_invite_code(self, session: str, id: str, **kwargs: Any) -> Any:
        """Gets the invite code for the group. (async)"""
        url = f"/api/{session}/groups/{id}/invite-code"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def revoke_invite_code(self, session: str, id: str, **kwargs: Any) -> Any:
        """Invalidates the current group invite code and generates a new one."""
        url = f"/api/{session}/groups/{id}/invite-code/revoke"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_revoke_invite_code(self, session: str, id: str, **kwargs: Any) -> Any:
        """Invalidates the current group invite code and generates a new one. (async)"""
        url = f"/api/{session}/groups/{id}/invite-code/revoke"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_participants(self, session: str, id: str, **kwargs: Any) -> Any:
        """Get participants"""
        url = f"/api/{session}/groups/{id}/participants"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_participants(self, session: str, id: str, **kwargs: Any) -> Any:
        """Get participants (async)"""
        url = f"/api/{session}/groups/{id}/participants"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_group_participants(self, session: str, id: str, **kwargs: Any) -> Any:
        """Get group participants."""
        url = f"/api/{session}/groups/{id}/participants/v2"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_group_participants(self, session: str, id: str, **kwargs: Any) -> Any:
        """Get group participants. (async)"""
        url = f"/api/{session}/groups/{id}/participants/v2"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def add_participants(
        self, session: str, id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Add participants"""
        url = f"/api/{session}/groups/{id}/participants/add"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_add_participants(
        self, session: str, id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Add participants (async)"""
        url = f"/api/{session}/groups/{id}/participants/add"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def remove_participants(
        self, session: str, id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Remove participants"""
        url = f"/api/{session}/groups/{id}/participants/remove"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_remove_participants(
        self, session: str, id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Remove participants (async)"""
        url = f"/api/{session}/groups/{id}/participants/remove"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def promote_to_admin(
        self, session: str, id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Promote participants to admin users."""
        url = f"/api/{session}/groups/{id}/admin/promote"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_promote_to_admin(
        self, session: str, id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Promote participants to admin users. (async)"""
        url = f"/api/{session}/groups/{id}/admin/promote"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def demote_to_admin(
        self, session: str, id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Demotes participants to regular users."""
        url = f"/api/{session}/groups/{id}/admin/demote"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_demote_to_admin(
        self, session: str, id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Demotes participants to regular users. (async)"""
        url = f"/api/{session}/groups/{id}/admin/demote"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class PresenceApi:
    """API Controller for Presence."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def set_presence(self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Set session presence"""
        url = f"/api/{session}/presence"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_set_presence(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Set session presence (async)"""
        url = f"/api/{session}/presence"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_presence_all(self, session: str, **kwargs: Any) -> Any:
        """Get all subscribed presence information."""
        url = f"/api/{session}/presence"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_presence_all(self, session: str, **kwargs: Any) -> Any:
        """Get all subscribed presence information. (async)"""
        url = f"/api/{session}/presence"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get_presence(self, session: str, chat_id: str, **kwargs: Any) -> Any:
        """Get the presence for the chat id. If it hasn't been subscribed - it also subscribes to it."""
        url = f"/api/{session}/presence/{chat_id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get_presence(self, session: str, chat_id: str, **kwargs: Any) -> Any:
        """Get the presence for the chat id. If it hasn't been subscribed - it also subscribes to it. (async)"""
        url = f"/api/{session}/presence/{chat_id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def subscribe(self, session: str, chat_id: str, **kwargs: Any) -> Any:
        """Subscribe to presence events for the chat."""
        url = f"/api/{session}/presence/{chat_id}/subscribe"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_subscribe(self, session: str, chat_id: str, **kwargs: Any) -> Any:
        """Subscribe to presence events for the chat. (async)"""
        url = f"/api/{session}/presence/{chat_id}/subscribe"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class ScreenshotApi:
    """API Controller for Screenshot."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def screenshot(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get a screenshot of the current WhatsApp session (**WEBJS/WPP** only)"""
        url = "/api/screenshot"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_screenshot(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get a screenshot of the current WhatsApp session (**WEBJS/WPP** only) (async)"""
        url = "/api/screenshot"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class EventsApi:
    """API Controller for Events."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def send_event(self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Send an event message"""
        url = f"/api/{session}/events"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_send_event(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Send an event message (async)"""
        url = f"/api/{session}/events"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class PingApi:
    """API Controller for Ping."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def ping(self, **kwargs: Any) -> Any:
        """Ping the server"""
        url = "/ping"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_ping(self, **kwargs: Any) -> Any:
        """Ping the server (async)"""
        url = "/ping"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class HealthApi:
    """API Controller for Health."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def check(self, **kwargs: Any) -> Any:
        """Check the health of the server"""
        url = "/health"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_check(self, **kwargs: Any) -> Any:
        """Check the health of the server (async)"""
        url = "/health"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class ServerApi:
    """API Controller for Server."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def get(self, **kwargs: Any) -> Any:
        """Get the version of the server"""
        url = "/api/server/version"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get(self, **kwargs: Any) -> Any:
        """Get the version of the server (async)"""
        url = "/api/server/version"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def environment(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get the server environment"""
        url = "/api/server/environment"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_environment(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Get the server environment (async)"""
        url = "/api/server/environment"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def status(self, **kwargs: Any) -> Any:
        """Get the server status"""
        url = "/api/server/status"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_status(self, **kwargs: Any) -> Any:
        """Get the server status (async)"""
        url = "/api/server/status"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def stop(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Stop (and restart) the server"""
        url = "/api/server/stop"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_stop(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Stop (and restart) the server (async)"""
        url = "/api/server/stop"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class ServerDebugApi:
    """API Controller for ServerDebug."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def cpu_profile(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Collect and return a CPU profile for the current nodejs process"""
        url = "/api/server/debug/cpu"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_cpu_profile(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Collect and return a CPU profile for the current nodejs process (async)"""
        url = "/api/server/debug/cpu"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def heapsnapshot(self, **kwargs: Any) -> Any:
        """Return a heapsnapshot for the current nodejs process"""
        url = "/api/server/debug/heapsnapshot"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_heapsnapshot(self, **kwargs: Any) -> Any:
        """Return a heapsnapshot for the current nodejs process (async)"""
        url = "/api/server/debug/heapsnapshot"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def browser_trace(self, session: str, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Collect and get a trace.json for Chrome DevTools"""
        url = f"/api/server/debug/browser/trace/{session}"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_browser_trace(self, session: str, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """Collect and get a trace.json for Chrome DevTools  (async)"""
        url = f"/api/server/debug/browser/trace/{session}"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class VersionApi:
    """API Controller for Version."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def get(self, **kwargs: Any) -> Any:
        """Get the server version"""
        url = "/api/version"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get(self, **kwargs: Any) -> Any:
        """Get the server version  (async)"""
        url = "/api/version"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class MediaApi:
    """API Controller for Media."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def convert_voice(self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Convert voice to WhatsApp format (opus)"""
        url = f"/api/{session}/media/convert/voice"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_convert_voice(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Convert voice to WhatsApp format (opus) (async)"""
        url = f"/api/{session}/media/convert/voice"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def convert_video(self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Convert video to WhatsApp format (mp4)"""
        url = f"/api/{session}/media/convert/video"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_convert_video(
        self, session: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any
    ) -> Any:
        """Convert video to WhatsApp format (mp4) (async)"""
        url = f"/api/{session}/media/convert/video"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class AppsApi:
    """API Controller for Apps."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def list(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """List all apps for a session"""
        url = "/api/apps"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_list(self, params: Optional[dict[str, Any]] = None, **kwargs: Any) -> Any:
        """List all apps for a session (async)"""
        url = "/api/apps"
        request_kwargs = {}
        if params is not None:
            request_kwargs["params"] = params
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def create(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Create a new app"""
        url = "/api/apps"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_create(self, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Create a new app (async)"""
        url = "/api/apps"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def get(self, id: str, **kwargs: Any) -> Any:
        """Get app by ID"""
        url = f"/api/apps/{id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_get(self, id: str, **kwargs: Any) -> Any:
        """Get app by ID (async)"""
        url = f"/api/apps/{id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("GET", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def update(self, id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Update an existing app"""
        url = f"/api/apps/{id}"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = self._http.request("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_update(self, id: str, payload: Optional[Union[dict[str, Any], Any]] = None, **kwargs: Any) -> Any:
        """Update an existing app (async)"""
        url = f"/api/apps/{id}"
        request_kwargs = {}
        if payload is not None:
            request_kwargs["json"] = (
                payload
                if isinstance(payload, dict)
                else (payload.model_dump() if hasattr(payload, "model_dump") else payload)
            )
        request_kwargs.update(kwargs)
        response = await self._http.arequest("PUT", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    def delete(self, id: str, **kwargs: Any) -> Any:
        """Delete an app"""
        url = f"/api/apps/{id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("DELETE", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_delete(self, id: str, **kwargs: Any) -> Any:
        """Delete an app (async)"""
        url = f"/api/apps/{id}"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("DELETE", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text


class McpApi:
    """API Controller for Mcp."""

    def __init__(self, http_client: WahaHttpClient) -> None:
        self._http = http_client

    def post(self, **kwargs: Any) -> Any:
        """POST /mcp"""
        url = "/mcp"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = self._http.request("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text

    async def a_post(self, **kwargs: Any) -> Any:
        """POST /mcp (async)"""
        url = "/mcp"
        request_kwargs = {}
        request_kwargs.update(kwargs)
        response = await self._http.arequest("POST", url, **request_kwargs)
        try:
            return response.json()
        except Exception:
            return response.text
