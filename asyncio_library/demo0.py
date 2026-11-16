import time,asyncio

#traditional - synchronous programming
def task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} completed")

task("A")
task("B")

#asynchronous programming
import asyncio

async def task1():
    print("Started")
    await asyncio.sleep(2)
    print("Completed")

asyncio.run(task1())

#async programming with co-routine
async def greet():
    return "Hello"

result = greet()

print(result)