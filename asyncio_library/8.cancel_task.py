import asyncio

async def worker():
    try:
        print("Worker started")
        await asyncio.sleep(10)
        print("Worker finished")
    except asyncio.CancelledError:
        print("Worker was cancelled")
        raise

async def main():
    task = asyncio.create_task(worker())

    await asyncio.sleep(2)

    print("Cancelling task...")
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Task cancellation confirmed")

asyncio.run(main())

