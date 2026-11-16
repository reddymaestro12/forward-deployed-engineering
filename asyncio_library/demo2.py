import time,asyncio

async def check_customer():
    print("checking customer")
    print("customer check completed")

#creating a coroutine object
coro = check_customer()

def main():
    check_customer()


#running the coroutine with normal function is not allowed 
asyncio.run(main())