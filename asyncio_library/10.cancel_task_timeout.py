import asyncio

async def long_running_task():
    await asyncio.sleep(10)
    return "Completed"

async def main():
    try:
        result = await asyncio.wait_for(
            long_running_task(),
            timeout=3
        )
        print(result)

    except asyncio.TimeoutError:
        print("Task timed out")

asyncio.run(main())