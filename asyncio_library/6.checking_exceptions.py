import asyncio

async def worker(n):
    if n == 3:
        raise RuntimeError("Worker failed")
    return n * 10

async def main():
    tasks = [worker(i) for i in range(5)]

    results = await asyncio.gather(
        *tasks,
        return_exceptions=True
    )

    for idx, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"Task {idx} failed: {result}")
        else:
            print(f"Task {idx} succeeded: {result}")

asyncio.run(main())