import aiohttp
import json
import asyncio


class API:

    def __init__(self):
        self._api = "https://blockchain.vsecoder.dev/api/"

    async def _request(
        self, url: str, method: str = "GET", data: dict = None, headers: dict = None
    ) -> dict:
        async with aiohttp.ClientSession() as session:
            async with session.request(
                method, url, data=data, headers=headers
            ) as response:
                return await response.json()

    async def create_wallet(self) -> dict:
        return await self._request(f"{self._api}bc/", "POST")

    async def get_wallet(self, public_key: str, private_key: str) -> dict:
        return await self._request(
            f"{self._api}bc?public_key={public_key}&private_key={private_key}"
        )

    async def transfer(self, from_: str, to: str, amount: float) -> dict:
        return await self._request(
            f"{self._api}bc/transfer?from_={from_}&to={to}&amount={amount}",
            "POST",
        )
