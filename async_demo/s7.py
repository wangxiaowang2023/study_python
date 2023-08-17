# -*- coding: utf-8 -*-
import asyncio
# asyncio.get_event_loop()
async def fun1():
    print('111')
    await asyncio.sleep(2)
    print('222')


print(fun1())
asyncio.run()