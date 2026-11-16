import threading
import time

def check_service(service_name):
    print(f"Checking {service_name} service")
    time.sleep(3)
    print(f"{service_name} service is up and running")

t =  threading.Thread(target=check_service, args=("Database",))
start = time.perf_counter() #time.time()
t.start()
t.join()
end = time.perf_counter()
print(f"Total Time Taken : {end - start} Seconds")

#without t.join()
print("Main thread is doing other work while the service check is running...")