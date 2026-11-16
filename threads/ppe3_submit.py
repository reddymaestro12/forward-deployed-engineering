from concurrent.futures import ProcessPoolExecutor

def cube(n):
    return n ** 3

if __name__ == "__main__":

    with ProcessPoolExecutor(max_workers=2) as executor:

        future1 = executor.submit(cube, 2)
        future2 = executor.submit(cube, 3)

        print(future1.result())
        print(future2.result())
