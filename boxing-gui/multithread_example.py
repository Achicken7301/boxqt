import threading
import time

# Shared variable
global count
count = 0

lock = threading.Lock()  # mutex


def print_time(thread_id, delay):
    global count  # use shared cariable

    for i in range(5):
        lock.acquire()
        count += 1
        lock.release()

        print(f"Thread {thread_id}: {count} ------{time.strftime('%M:%S')}")
        time.sleep(delay)


# Data prepare
threads = list()
threads.append(threading.Thread(target=print_time, args=(1, 1)))  # args = (thread_id, delay))
threads.append(threading.Thread(target=print_time, args=(2, 2)))

# Start
for thread in threads:
    thread.start()

# Wait for threads finished
for thread in threads:
    thread.join()