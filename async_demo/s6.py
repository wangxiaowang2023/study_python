# -*- coding: utf-8 -*-
import asyncio



async def f1():
    print(1)
    await asyncio.sleep(2)
    print(2)


async def f2():
    print(3)
    await asyncio.sleep(2)
    print(4)


task = [
    asyncio.ensure_future(f1()), asyncio.ensure_future(f2())
]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(task))
# -*- coding: utf-8 -*-
