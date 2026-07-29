import pytest

from waha import AsyncWahaClient, WahaClient


def test_client_init():
    client = WahaClient("http://localhost:3000", api_key="secret-key")
    assert client._http.base_url == "http://localhost:3000"
    assert client._http.api_key == "secret-key"
    assert hasattr(client, "chatting")
    assert hasattr(client, "sessions")
    assert hasattr(client, "auth")
    client.close()


@pytest.mark.anyio
async def test_async_client_init():
    client = AsyncWahaClient("http://localhost:3000", api_key="secret-key")
    assert client._http.base_url == "http://localhost:3000"
    assert hasattr(client, "chatting")
    assert hasattr(client, "sessions")
    await client.close()
