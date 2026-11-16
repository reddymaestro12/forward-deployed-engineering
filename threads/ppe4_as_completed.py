from concurrent.futures import ProcessPoolExecutor, as_completed
import time

def task(seconds):
    time.sleep(seconds)
    return f"Finished {seconds}"

if __name__ == "__main__":

    with ProcessPoolExecutor(max_workers=3) as executor:

        futures = [
            executor.submit(task, 3),
            executor.submit(task, 1),
            executor.submit(task, 2)
        ]

        for future in as_completed(futures):
            print(future.result())