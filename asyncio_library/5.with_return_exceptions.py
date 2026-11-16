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
        task2(),
        return_exceptions=True
    )
    for result in results:
        if isinstance(result, Exception):
            print(f"Task raised an exception: {result}")
        else:
            print(f"Task completed successfully: {result}")

asyncio.run(main())