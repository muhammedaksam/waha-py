# waha-py

[![PyPI version](https://img.shields.io/pypi/v/waha-py.svg)](https://pypi.org/project/waha-py/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)

Python SDK for [WAHA (WhatsApp HTTP API)](https://github.com/devlikeapro/waha) - auto-generated from OpenAPI spec with full type safety, Pydantic v2 models, and HTTPX-based synchronous & asynchronous clients.

## Installation

```bash
pip install waha-py
```

## Usage

### Synchronous Client

```python
from waha import WahaClient

# Initialize with baseURL and optional API key
client = WahaClient("http://localhost:3000", api_key="your-api-key")

# Access controllers via properties
# Sessions
sessions = client.sessions.list()

# Chatting
message = client.chatting.send_text(
    session="default",
    payload={
        "chatId": "1234567890@c.us",
        "text": "Hello from waha-py!",
    },
)

# Get QR Code
qr = client.auth.get_qr(session="default", params={"format": "raw"})

# Always close client when done
client.close()
```

### Asynchronous Client

```python
import asyncio
from waha import AsyncWahaClient


async def main():
    async_client = AsyncWahaClient("http://localhost:3000", api_key="your-api-key")

    # Send message asynchronously
    message = await async_client.chatting.a_send_text(
        session="default",
        payload={
            "chatId": "1234567890@c.us",
            "text": "Async hello from waha-py!",
        },
    )

    await async_client.close()


asyncio.run(main())
```

## API Controllers

All endpoints are available through client properties:

```python
client.sessions.*      # SessionsApi
client.chatting.*      # ChattingApi
client.contacts.*      # ContactsApi
client.groups.*        # GroupsApi
client.auth.*          # AuthApi
client.labels.*        # LabelsApi
client.presence.*      # PresenceApi
client.profile.*       # ProfileApi
client.media.*         # MediaApi
# ...and more
```

## Pydantic Models

All types are auto-generated from the WAHA OpenAPI specification using Pydantic v2:

```python
from waha.generated.models import SessionInfo, MessageTextRequest, WAMessage
```

## How It Works

This package is automatically kept in sync with WAHA:

1. **Daily** - GitHub Action spins up latest `devlikeapro/waha` container
2. **Fetches** OpenAPI spec from `/-json` endpoint
3. **Compares** SHA256 hash with committed `openapi.json`
4. **If changed** - Generates new types + Python clients, bumps version, commits, and pushes tag
5. **Publishes** to PyPI via OIDC trusted publishing

## Development

### Prerequisites

- Python >= 3.9
- Running WAHA instance (or `openapi.json`)

### Generate Types & Clients Locally

```bash
# Install development dependencies
pip install -e ".[dev]"

# Generate models and clients from openapi.json
python scripts/generate.py

# Run tests
pytest
```

## License

MIT
