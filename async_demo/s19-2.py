# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import asyncio
from concurrent.futures import ThreadPoolExecutor
import time

def download_file(url=None):
    print(f"下载图片={url}")
    time.sleep(1)
    print(f"下载完成={url}")


async def main():
    executor = ThreadPoolExecutor(5)

    loop =  asyncio.get_running_loop()
    tasks = []
    for i in range(1,11):
        t = loop.run_in_executor(executor,download_file,i)
        tasks.append(t)
    await asyncio.wait(tasks)

asyncio.run(main())