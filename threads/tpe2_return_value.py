from concurrent.futures import ThreadPoolExecutor

def square(n):
    return n * n

with ThreadPoolExecutor(max_workers=3) as executor:
    future = executor.submit(square, 5)

    result = future.result()

print(result)