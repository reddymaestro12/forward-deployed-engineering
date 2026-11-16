from multiprocessing import Process, Queue

def worker(numbers, q):
    output = []

    for n in numbers:
        output.append(n*n)

    q.put(output)

if __name__ == "__main__":

    q = Queue()

    data = list(range(10))

    p1 = Process(target=worker, args=(data[:5], q))
    p2 = Process(target=worker, args=(data[5:], q))

    p1.start()
    p2.start()

    result1 = q.get()
    result2 = q.get()

    p1.join()
    p2.join()

    final_result = result1 + result2

    print(final_result)