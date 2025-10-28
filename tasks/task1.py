import aiohttp
import asyncio

async def fetch_status(session, url):
    async with session.get(url) as response:
        return response.status



async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_status(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results


async def main():
    async with aiohttp.ClientSession() as session:
        print(await fetch_status(session, "https://httpbin.org/status/200"))

