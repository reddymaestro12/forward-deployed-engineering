#used for parallel data processing

from multiprocessing import Process, Queue
import time

#without multiprocessing, the tasks will be executed sequentially, which can be time-consuming for large datasets. By using multiprocessing, we can distribute the workload across multiple CPU cores, allowing for faster processing and improved performance.
#Suppose you need to square one million numbers.

def square_numbers(numbers, result_queue):
    for number in numbers:
        result_queue.put(number * number)

if __name__ == '__main__':
    numbers = list(range(1, 1000001))  # One million numbers
    result_queue = Queue()
    processes = []

    # Create 4 processes
    for i in range(4):
        start = i * len(numbers) // 4
        end = (i + 1) * len(numbers) // 4
        process = Process(target=square_numbers, args=(numbers[start:end], result_queue))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    # Collect results
    squared_numbers = []
    while not result_queue.empty():
        squared_numbers.append(result_queue.get())

    print(f"First 10 squared numbers: {squared_numbers[:10]}")