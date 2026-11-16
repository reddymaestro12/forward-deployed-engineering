#Sometimes you want results as soon as they finish.
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def task(n):
    time.sleep(n)
    return f"Task {n}"

with ThreadPoolExecutor(max_workers=3) as executor:
    futures=[
        executor.submit(task,3),
        executor.submit(task,1),
        executor.submit(task,2)
    ]
    for future in as_completed(futures):
        print(future.result())