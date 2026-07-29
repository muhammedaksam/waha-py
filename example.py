import asyncio

from waha import AsyncWahaClient, WahaClient


def sync_example():
    print("=== Sync Example ===")
    client = WahaClient("http://localhost:3000", api_key="secret")
    print("Initialized WahaClient successfully.")
    print("Available controllers:", [attr for attr in dir(client) if not attr.startswith("_")])
    client.close()


async def async_example():
    print("\n=== Async Example ===")
    async_client = AsyncWahaClient("http://localhost:3000", api_key="secret")
    print("Initialized AsyncWahaClient successfully.")
    await async_client.close()


if __name__ == "__main__":
    sync_example()
    asyncio.run(async_example())
