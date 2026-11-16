import time,threading

counter =0
def increment_counter():
    global counter
    for i in range(1000):
        current_value = counter
        time.sleep(0)
        counter = current_value + 1

threads =[
    threading.Thread(target=increment_counter),
    threading.Thread(target=increment_counter)
    
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Final Counter Value : {}".format(counter))
print(f"actual counter value should be 2000 but due to race condition it is {counter} which is less than 2000")

"""
A race condition occurs when multiple threads access and modify shared data (shared memory) at the same time, and the final result depends on the unpredictable order in which the threads execute.

Since thread scheduling is controlled by the operating system, you cannot guarantee which thread runs first. This can lead to incorrect or inconsistent results.
"""