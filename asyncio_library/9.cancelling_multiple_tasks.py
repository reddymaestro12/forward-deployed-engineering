import asyncio

async def worker(name):
    try:
        while True:
            print(f"{name} working...")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print(f"{name} cancelled")
        raise

async def main():
    tasks = [
        asyncio.create_task(worker("A")),
        asyncio.create_task(worker("B")),
        asyncio.create_task(worker("C"))
    ]

    await asyncio.sleep(3)

    print("Cancelling all tasks")

    for task in tasks:
        task.cancel()

    results = await asyncio.gather(
        *tasks,
        return_exceptions=True
    )

    print(results)

asyncio.run(main())