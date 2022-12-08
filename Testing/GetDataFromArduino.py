from ast import If
from random import sample
from socket import if_nameindex
import serial
import serial.tools.list_ports
import time


def serial_ports():
    port = []
    cp = serial.tools.list_ports.comports()
    for p in cp:
        if "BTHENUM" in p.hwid:
            start_of_address = p.hwid.rfind("&")
            end_of_address = p.hwid.rfind("_")
            address = p.hwid[start_of_address + 1:end_of_address]
            if int(address, 16) == 0:
                port_type = "incoming"
            else:
                port_type = "outgoing"
            # get Outgoing ports ONLY
            if port_type == "outgoing":
                port.append(p.name)
    return port


ports = serial_ports()
print(ports)

ser = serial.Serial(port="COM6", baudrate=1000000)
# ser = serial.Serial(port='COM13', baudrate=115200)

b = ser.readline()

# now = time.time()
start = time.time()
# future = now + 1
i = 0
data = []
samples = 20
while i < samples:
    # do stuff
    b = ser.readline()
    data_ser = b.decode().splitlines()
    data.append(data_ser)
    i += 1
    # print(str(future - now))
# # print(data)
# end = time.time()
# print(end - start)
# print("sample rate: " + str(float(samples) / (end - start)))
print(type(data))

ser.close()