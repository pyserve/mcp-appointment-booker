from typing import Any

import httpx

API_BASE_URL = "http://localhost:8000"
USER_AGENT = "appointment-booker/1.0"


async def api_request(relative_url: str) -> dict[str, Any] | None:
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    url = f"{API_BASE_URL}{relative_url}"

    async with httpx.AsyncClient() as client:
        try:
            res = await client.get(url, headers=headers, timeout=60.0)
            res.raise_for_status()
            return res.json()
        except Exception:
            return None
