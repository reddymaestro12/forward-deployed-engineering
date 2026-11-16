from concurrent.futures import ProcessPoolExecutor

def transform(num):
    return num ** 2

if __name__ == "__main__":

    data = range(100)

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(transform, data))
    print(results[:10])  # Print the first 10 results for verification