from concurrent.futures import ProcessPoolExecutor

def square(n):
    return n * n

with ProcessPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(square, [1, 2, 3, 4]))

print(results)