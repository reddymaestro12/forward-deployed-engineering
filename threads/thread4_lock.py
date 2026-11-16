import time,threading

counter =0
current_lock = threading.Lock()

def increment_counter():
    global counter
    for i in range(1000):
        with current_lock:
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
print(f"actual counter value should be 2000 and due to lock it is {counter} which is equal to 2000")