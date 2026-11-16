import multiprocessing,time,os

def analyze_image(image_name,result_queue):
    print(f"image name: {image_name} is being processed ")
    people_detector = 4
    result_queue.put({
        "image_name": image_name,
        "people_detected": people_detector
    })

if __name__ == '__main__':
    result_queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=analyze_image, args=("image001.png", result_queue))
    process.start()
    print("main process started")
    process.join()
    print("main process completed")
    print("result from child process: ", result_queue.get())