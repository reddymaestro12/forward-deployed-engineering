import time
import os 

def read_customer():
    print("Reading customer data from database")
    time.sleep(3)
    print("Reading customer data completed")

def fetch_customer():
    print("Fetching customer data from database")
    time.sleep(3)
    print("Fetching customer data completed")

def run_prediction():
    print("Running prediction on customer data")
    time.sleep(3)
    print("Prediction completed")

start = time.time()
read_customer()
fetch_customer()
run_prediction()
end = time.time()   
print("Total Time Taken : {} Seconds".format (end-start))