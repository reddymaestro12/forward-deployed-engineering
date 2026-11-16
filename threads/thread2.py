import threading
import time

def check_service(service_name):
    print(f"Checking {service_name} service")
    time.sleep(3)
    print(f"{service_name} service is up and running")

services = ["Database", "Web Server", "Cache"]
threads = []
start = time.perf_counter() #time.time()

for service in services:
    t = threading.Thread(target=check_service, args=(service,))
    threads.append(t)
    t.start()   
    
for t in threads:
    t.join()

elaspse = time.perf_counter() - start
#print(f"Total Time Taken : {elaspse} Seconds")

print(f"all checks are completed  {elaspse} Seconds, main thread is doing other work while the service checks are running...")
