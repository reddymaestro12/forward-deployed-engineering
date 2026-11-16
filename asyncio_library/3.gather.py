import asyncio,time

async def check_service(service_name):
    try:
        print(f"checking {service_name}")
        await asyncio.sleep(2)
        print(f"{service_name} is healthy")
        print("Health: OK")
    except Exception as e:
        print(f"Error checking {service_name}: {e}")
        print("Health: NOT OK")
    return f"{service_name} check completed"

async def main():
    start_time = time.perf_counter()

    #run all the coroutines concurrently
    results = await asyncio.gather(check_service("Service A"), check_service("Service B"), check_service("Service C"))
    for result in results:
        print(f"Result: {result}")
    end_time = time.perf_counter()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")


asyncio.run(main())