import httpx
from app.config import API_BASE_URL

async def fetch_keys():
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{API_BASE_URL}/keys")
        r.raise_for_status()
        return r.json()

async def fetch_stats():
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{API_BASE_URL}/stats")
        r.raise_for_status()
        return r.json()
