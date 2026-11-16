import time,asyncio

async def check_customer():
    print("checking customer")
    print("customer check completed")

#creating a coroutine object
coro = check_customer()

async def main():
    await check_customer()

#running the coroutine with 
asyncio.run(main())