from threading import Thread, Lock, current_thread
from queue import Queue
import time

db = 0

def db_increment(lock):
    global db
    lock.acquire() # lock a thread
    local_db_copy = db
    # processing
    local_db_copy += 1
    time.sleep(0.1)
    db = local_db_copy
    lock.release() # unlock a thread; always release a lock thread else you get stuck

if __name__ == "__main__":
    lock = Lock() # Prevent race conditions
    print(f"Starting database value: {db}")
    thread1 = Thread(target=db_increment, args=(lock,))
    thread2 = Thread(target=db_increment, args=(lock,))

    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    print(f"Ending database value: {db}")


# Queue is safe for multiple concurrent (thread and process)

# Queue is a linear data structure that follows the FIFO (First In First Out) algorithm
# Example: A queue of customers that are waiting for ATM services

def customer(qu, lock):
    while True:
        value = qu.get()
        # processing
        with lock:
            print(f"In current thread: {current_thread().name} got {value}")
        qu.task_done()

if __name__ == '__main__':
    qu = Queue()
    lock = Lock() # Prevent race conditions
    num_threads = 10
    for i in range(num_threads):
        thread = Thread(target=customer, args = (qu, lock,))
        thread.daemon = True # Daemon thread is a thread that will die when the main thread dies
        thread.start()
    
    for c in range(1, 31):
        qu.put(c)
    qu.join()
    print("End process")
    
    # Number of customers waiting
    # qu.put(1)
    # qu.put(2)
    # qu.put(3)
    # qu.put(4)
    # qu.put(5)
    
    # # 5 4 3 2 1 --> Waiting for ATM services
    # first = qu.get()
    # print(first) # This will return the first customer in a queue and remove him
    # print("End")
    # qu.task_done() # This tells the queue that we are done processing customers
