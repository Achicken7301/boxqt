import time

while 1:
    start = time.time()
    time.sleep(0.1)
    end = time.time()
    print("sleep:" + str(end - start))
