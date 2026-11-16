import multiprocessing,time,os

def read_customer():
    print("child process started")
    time.sleep(3)
    print("child process completed")



if __name__ == '__main__':
    process = multiprocessing.Process(target=read_customer)
    start = time.time()
    
    process.start()
    print("main process started")
    process.join()
    print("main process completed: child has finished")
    end = time.time()
    print("Total Time Taken : {} Seconds".format (end-start))