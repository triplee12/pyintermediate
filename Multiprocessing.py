from multiprocessing import Process, Value, Array, Lock, Pool
import os
import time


__author__ = "Ejie Emmanuel Ebuka"


# Multiprocessing

def square():
    for i in range(2):
        i = i
        time.sleep(0.1)

my_processes = []
num_processes = os.cpu_count() # number of CPUs available on the machine
# Create processes and asign a function to each process.
for i in range(num_processes):
    process = Process(target = square)
    my_processes.append(process)
# Start all processes
for p in my_processes:
    p.start()
# Join process
# Wait for all processes to finish
# block the main program until all processes have finished
for p in my_processes:
    p.join()
print("End process")


# Single processing: share a single process values
def add_num(num, lock):
    for _ in range(100):
        time.sleep(0.01)
        # the best way to use lock is as context manager
        with lock:
            num += 1

if __name__ == "__main__":
    lock = Lock()
    shared_value = Value("i", 0)
    print(f"Starting number is {shared_value.value}")
    
    # Let's two processes that will modify one
    process1 = Process(target=add_num, args=(shared_value,lock))
    process2 = Process(target=add_num, args=(shared_value,lock))
    
    process1.start()
    process2.start()
    
    process1.join()
    process2.join()
    
    print(f"Ending number is {shared_value.value}")


# Share array values

def add_arry(numbers, lock):
    for _ in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            # the best way to use lock is as context manager
            with lock:
                numbers[i] += 1

if __name__ == "__main__":
    lock = Lock()
    shared_array = Array("d", [0.0, 100.0, 200.0, 300.0])
    print(f"Starting array is {shared_array[:]}")
    
    # Let's two processes that will modify one
    process1 = Process(target=add_num, args=(shared_array,lock))
    process2 = Process(target=add_num, args=(shared_array,lock))
    
    process1.start()
    process2.start()
    
    process1.join()
    process2.join()
    
    print(f"Ending array is {shared_array[:]}")

# Process Pool
# A process pool can be used to manage multiple processes
def cube(number):
    return number * number * number

if __name__ == '__main__':
    number = range(5)
    pool = Pool()
    # four important methods: map, apply, join, and close
    result = pool.map(cube, number) # This will split the data into chunks
    # pool.apply(cube, number[0]) # This will only excute the first chunk
    pool.close()
    pool.join()
    print(result)
