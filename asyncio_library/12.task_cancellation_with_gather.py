import asyncio

async def worker(name):
    try:
        await asyncio.sleep(10)
        return name
    except asyncio.CancelledError:
        print(f"{name} cancelled")
        raise

async def main():
    tasks = [asyncio.create_task(worker(f"Task-{i}"))
             for i in range(3)]

    await asyncio.sleep(2)

    tasks[1].cancel()

    results = await asyncio.gather(
        *tasks,
        return_exceptions=True
    )

    for r in results:
        print(type(r).__name__, r)

asyncio.run(main())