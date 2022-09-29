import serial
import serial.tools.list_ports
import time

# print(serial.version)
ser = serial.Serial(port='COM7', baudrate=115200)
# ser = serial.Serial(port='COM13', baudrate=115200)

b = ser.readline()

now = time.time()
future = now + 1
data = []
while now < future:
    # do stuff
    now = time.time()
    b = ser.readline()
    data_ser = b.decode().splitlines()
    data.append(data_ser)
    print(str(future - now))
# print(data)
print("Sample rate: " + str(len(data)))
