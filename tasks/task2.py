import asyncio


async def delayed_echo(text, delay):
   await asyncio.sleep(delay)
   return text

async def echo_all():
    result = [
        delayed_echo('hello', 2),
        delayed_echo('world', 2),
        delayed_echo('!', 2)
    ]

    return await asyncio.gather(*result)
