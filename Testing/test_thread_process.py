import time
import concurrent.futures
import threading
from random import sample
import serial
import serial.tools.list_ports
import time
import pandas as pd

ser = serial.Serial(port="COM6", baudrate=1000 * 1000)

lock = threading.Lock()  # mutex
global state
state =  1

# INPUT
def state_status():
    global state
    while 1:
        state = int(input("State input: "))

# OUTPUT
def outputUser():
    while  1:
        if state == True:
            print("state = 1")
        else:
            print("state = 0")
        
        time.sleep(1)

def getData(delay):
    while state:
        # print("HELLO " + str(delay))
        try:
            # lock.acquire()
            b = ser.readline()
            data_ser = b.decode().splitlines()
            data.append(data_ser)
            # lock.release()
        except Exception as e:
            print(e)
        time.sleep(delay)


def printData(delay):
    for _ in range(5):
        print(len(data))
        print(data)
        time.sleep(delay)


# Data prepare
threads = list()
# threads.append(threading.Thread(target=getData, args=(1, )))
# threads.append(threading.Thread(target=printData, args=(2, )))
threads.append(threading.Thread(target=state_status))
threads.append(threading.Thread(target=outputUser))

# Start
for thread in threads:
    thread.start()

# Wait for threads finished
for thread in threads:
    thread.join()

ser.close()
