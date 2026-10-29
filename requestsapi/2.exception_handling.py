import os
def exception_handling(a,b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error")
    else:
        print(f"result is {result}")
    finally:
        print("closing the resources")
        

exception_handling(10,0)