import aiohttp
import asyncio

async def fetch_liquidity(exchange, token):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{exchange['url']}/liquidity/{token}", timeout=5) as response:
            return await response.json()

class ExchangeIntegration:
    def __init__(self):
        self.exchanges = {
            "pump_fun": {"url": "https://api.pump.fun"},
            "jupiter": {"url": "https://api.jup.ag"},
            "meteora": {"url": "https://api.meteora.ag"},
            "raydium": {"url": "https://api.raydium.io"}
        }

    async def get_best_exchange(self, token):
        best_exchange = None
        best_liquidity = 0

        tasks = [fetch_liquidity(exchange, token) for exchange in self.exchanges.values()]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        for exchange, liquidity in zip(self.exchanges.keys(), results):
            if not isinstance(liquidity, Exception) and liquidity > best_liquidity:
                best_liquidity = liquidity
                best_exchange = exchange

        return best_exchange