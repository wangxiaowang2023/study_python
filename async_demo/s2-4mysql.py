# -*- coding: utf-8 -*-
import asyncio
import aiomysql


async def main():
    conn = await aiomysql.connect(
        host="172.17.0.1",
        user='root',
        password="root",
        db='mysql',
        port=3307
    )
    # 创建CURSOR
    cur = await conn.cursor()
    # 执行SQL
    await cur.execute("SELECT Host,User FROM user")
    # 获取SQL结果
    result = await cur.fetchall()
    print(result)
    # 关闭CURSOR
    await cur.close()
    # 关闭连接
    conn.close()

main()
asyncio.run(main())
