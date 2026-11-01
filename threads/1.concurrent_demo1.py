import urllib.request
import time

start = time.time()
req = urllib.request.urlopen('https://www.tutorialspoint.com')
pahehtml = req.read()
end = time.time()
print("Page Fetching Time : {} Seconds".format (end-start))