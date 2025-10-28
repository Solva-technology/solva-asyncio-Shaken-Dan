import asyncio


async def safe_divide(a, b):
    await asyncio.sleep(0.1)

    if b == 0:
        e = ZeroDivisionError('Ошибка деления')
        return str(e)
    else:
        return round(a/b, 1)

async def run_divisions():
    divisions = [
        safe_divide(10, 2),
        safe_divide(2, 0),
        safe_divide(10, 5)
    ]

    return await asyncio.gather(*divisions)
