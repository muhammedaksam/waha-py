from typing import Optional

from .generated.api import (
    ApiKeysApi,
    AppsApi,
    AuthApi,
    CallsApi,
    ChannelsApi,
    ChatsApi,
    ChattingApi,
    ContactsApi,
    ContactsSessionApi,
    EventsApi,
    GroupsApi,
    HealthApi,
    LabelsApi,
    LidsApi,
    McpApi,
    MediaApi,
    PingApi,
    PresenceApi,
    ProfileApi,
    ScreenshotApi,
    ServerApi,
    ServerDebugApi,
    SessionsApi,
    StatusApi,
    VersionApi,
)
from .http import WahaHttpClient


class WahaClient:
    """Synchronous WAHA Client providing access to all API controllers."""

    def __init__(
        self,
        base_url: str,
        api_key: Optional[str] = None,
        headers: Optional[dict[str, str]] = None,
        timeout: float = 60.0,
        http_client: Optional[WahaHttpClient] = None,
    ) -> None:
        self._http = http_client or WahaHttpClient(base_url=base_url, api_key=api_key, headers=headers, timeout=timeout)

        self.auth = AuthApi(self._http)
        self.api_keys = ApiKeysApi(self._http)
        self.sessions = SessionsApi(self._http)
        self.profile = ProfileApi(self._http)
        self.chatting = ChattingApi(self._http)
        self.chats = ChatsApi(self._http)
        self.calls = CallsApi(self._http)
        self.channels = ChannelsApi(self._http)
        self.status = StatusApi(self._http)
        self.labels = LabelsApi(self._http)
        self.contacts = ContactsApi(self._http)
        self.contacts_session = ContactsSessionApi(self._http)
        self.lids = LidsApi(self._http)
        self.groups = GroupsApi(self._http)
        self.presence = PresenceApi(self._http)
        self.screenshot = ScreenshotApi(self._http)
        self.events = EventsApi(self._http)
        self.ping = PingApi(self._http)
        self.health = HealthApi(self._http)
        self.server = ServerApi(self._http)
        self.server_debug = ServerDebugApi(self._http)
        self.version = VersionApi(self._http)
        self.media = MediaApi(self._http)
        self.apps = AppsApi(self._http)
        self.mcp = McpApi(self._http)

    def close(self) -> None:
        self._http.close()


class AsyncWahaClient:
    """Asynchronous WAHA Client providing access to all API controllers."""

    def __init__(
        self,
        base_url: str,
        api_key: Optional[str] = None,
        headers: Optional[dict[str, str]] = None,
        timeout: float = 60.0,
        http_client: Optional[WahaHttpClient] = None,
    ) -> None:
        self._http = http_client or WahaHttpClient(base_url=base_url, api_key=api_key, headers=headers, timeout=timeout)

        self.auth = AuthApi(self._http)
        self.api_keys = ApiKeysApi(self._http)
        self.sessions = SessionsApi(self._http)
        self.profile = ProfileApi(self._http)
        self.chatting = ChattingApi(self._http)
        self.chats = ChatsApi(self._http)
        self.calls = CallsApi(self._http)
        self.channels = ChannelsApi(self._http)
        self.status = StatusApi(self._http)
        self.labels = LabelsApi(self._http)
        self.contacts = ContactsApi(self._http)
        self.contacts_session = ContactsSessionApi(self._http)
        self.lids = LidsApi(self._http)
        self.groups = GroupsApi(self._http)
        self.presence = PresenceApi(self._http)
        self.screenshot = ScreenshotApi(self._http)
        self.events = EventsApi(self._http)
        self.ping = PingApi(self._http)
        self.health = HealthApi(self._http)
        self.server = ServerApi(self._http)
        self.server_debug = ServerDebugApi(self._http)
        self.version = VersionApi(self._http)
        self.media = MediaApi(self._http)
        self.apps = AppsApi(self._http)
        self.mcp = McpApi(self._http)

    async def close(self) -> None:
        await self._http.aclose()
