from multiprocessing import Process
from threading import Thread
import os
import time


__author__ = "Ejie Emmanuel Ebuka"

# Threading Vs Multiprocessing

"""
With threading Vs multiprocessing you can run code in parallel

Multiprocess: An instance of a program (e.g Python interpreter)

+ Takes advantage of multiple CPUs and cores
+ Separate memory space -> Memory is not shared between processes
+ Great for CPU-bound processing
+ New process is started independently from other processes
+ Processes are interruptable/killable
+ One GIL for each process -> avoids GIL limitation

- Heavyweight
- Starting a process is slower than starting a thread.
- More memory
-IPC (inter-process communication) is more complicated



Thread: An entity within a process that can be scheduled (also knwon as "leightweight process)
A process can spawn multiple threads.

+ All threads within a process share the same memory
+ Leightweight
+ Starting a thread is faster than starting a process.
+ Great for I/O-bound tasks

- Threading is limited by GIL: Only one thread at a time
- No effect for CPU-bound tasks
- Not interruptable/killable
- Careful with race conditions

GIL: Global Interpreter Lock

- A lock that allows only one thread at a time to execute in Python
- Needed in CPython because of memory management is not thread safe

- Avoid:
    - Use multiprocessing
    - Use a different, free-threaded Python implementation (Jython, IronPython)
    - Use Python as a wrapper for third-party libraries (c/c++) -> numpy, scipy
"""

# Multiprocessing

def square():
    for i in range(2):
        i = i
        time.sleep(0.2)

my_processes = []
num_processes = os.cpu_count()
# Create processes
for i in range(num_processes):
    process = Process(target = square)
    my_processes.append(process)
# Start process
for p in my_processes:
    p.start()
# Join process
for p in my_processes:
    p.join()
print("End process")


# Multithreading
my_threads = []
num_threads = 10
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
