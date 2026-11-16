#Running Multiple Coroutines

#without asyncio 
print("******************** without asyncio ********************")
import time

def work1():
    time.sleep(2)

for _ in range(3):
    work1()


#with asyncio
print("******************** with asyncio ********************")
import asyncio

async def work(name):
    print(f"{name} started")
    await asyncio.sleep(2)
    print(f"{name} completed")

async def main():
    await asyncio.gather(
        work("A"),
        work("B"),
        work("C")
    )

asyncio.run(main())