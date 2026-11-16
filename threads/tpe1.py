from concurrent.futures import ThreadPoolExecutor
import time

def worker(n):
    print(f"Worker {n} is starting")
    time.sleep(2)
    print(f"Worker {n} has finished")

with ThreadPoolExecutor(max_workers=3) as executor:
    for i in range(5):
        executor.submit(worker, i)

print("All tasks have been completed")