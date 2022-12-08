from warnings import catch_warnings
import serial
import serial.tools.list_ports
import time

vcc = float(3.3)
r0 = 1000.0
ser = serial.Serial(port="COM6", baudrate=9600)

def map( x,  in_min,  in_max,  out_min,  out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def fsr(vol):
     vcc = 3.3
     r0 = 1000.0   
     rFSR = vcc / float(vol)
     rFSR = rFSR - 1
     rFSR = r0 * rFSR
     return rFSR

start = time.time()
while True:
    m = 0
    
    
    b = ser.readline()
    data_ser = b.decode().splitlines()
    vol = float(map(float(data_ser[0]), 0, 4095, 0, 3.3))
    if (vol == 0):
        vol = 0.0000001
    # print("analog: " + str(data_ser[0]) + " vol: " + str(vol))
    
    # vcc / vmeas
    # m = vcc / vol
    # m = m - 1
    # m = r0 * m
    # m = 271000.0 / m
    # m = pow(m, 1 / 0.69)
    
    rFSR = fsr(vol)
    m = 538.65 * rFSR
    m = 271000.0*1050 / m
    m = pow(m, 1 / 0.69)
    
    m /= 1000
    print("vol: " + str(vol) + " mass: " + str(m)+"kg")
    if (time.time() - start > 5):
        print("Close")
        ser.close()
        break

# print(m)