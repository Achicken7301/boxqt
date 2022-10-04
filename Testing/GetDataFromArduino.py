from traceback import print_tb
import serial
import serial.tools.list_ports
import time

# print(serial.version)
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

ser = serial.Serial(port='COM6', baudrate=115200)
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
print(data[0])
ser.close()
