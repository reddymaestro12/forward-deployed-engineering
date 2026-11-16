import asyncio

async def worker():
    await asyncio.sleep(5)

async def main():
    task = asyncio.create_task(worker())

    await asyncio.sleep(1)
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        pass

    print(task.cancelled())

asyncio.run(main())