import asyncio

async def task1():
    await asyncio.sleep(1)
    return "Task 1 completed"

async def task2():
    await asyncio.sleep(2)
    raise ValueError("Something went wrong")

async def main():
    results = await asyncio.gather(
        task1(),
        task2()
    )
    print(results)

asyncio.run(main())