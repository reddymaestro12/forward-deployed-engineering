import asyncio

async def check_customer(cust_no):
    print(f"checking customer {cust_no}")
    #do test by commenting this line and observe the output
    await asyncio.sleep(2)
    print(f"customer check {cust_no} completed")

async def main():
    #creating a coroutine object
    coro1 = asyncio.create_task(check_customer(1))
    coro2 = asyncio.create_task(check_customer(2))
    coro3 = asyncio.create_task(check_customer(3))

    #run all the coroutines concurrently
    await asyncio.gather(coro1, coro2, coro3)

asyncio.run(main())