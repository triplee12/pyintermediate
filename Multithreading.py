from threading import Thread
import time


__author__ = "Ejie Emmanuel Ebuka"

# Multithreading
my_threads = []
num_threads = 10

def square():
    for i in range(2):
        i = i
        time.sleep(0.2)

# Create threads
for i in range(num_threads):
    thread = Thread(target = square)
    my_threads.append(thread)
# Start thread
for t in my_threads:
    t.start()
# Join thread
for t in my_threads:
    t.join()
print("End thread")