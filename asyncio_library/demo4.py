import time,asyncio

async def check_customer():
    print("checking customer")
    print("customer check completed")



async def main():
    await check_customer()
    await check_customer()
    await check_customer()

#running the coroutine with  multiple await statements
asyncio.run(main())