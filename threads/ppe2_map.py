from concurrent.futures import ProcessPoolExecutor
import os

def worker(n):
    print(f"Processing {n} in PID {os.getpid()}")
    return n * n

if __name__ == "__main__":

    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(worker, [1,2,3,4,5]))

    print(results)