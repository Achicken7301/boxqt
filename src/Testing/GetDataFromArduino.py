import matplotlib.pyplot as plt
import time
import pandas as pd
import datetime
import serial

ser = serial.Serial(port='COM6', baudrate=115200)
current_time = datetime.datetime.now()
millis = []
acceleration_x = []
acceleration_y = []
acceleration_z = []
gyroscope_x = []
gyroscope_y = []
gyroscope_z = []
value_quantity = 500

for i in range(value_quantity):
    b = ser.readline()
    # Cannot decode the 1st value b'\xb4j7\r\n'
    # solve this with try except
    try:
        string_n = b.decode()

        print(string_n)
        # time.sleep(2)
        [a_x, a_y, a_z, g_x, g_y, g_z] = string_n.split()
        # millis.append(float(t))
        acceleration_x.append(float(a_x))
        acceleration_y.append(float(a_y))
        acceleration_z.append(float(a_z))
        gyroscope_x.append(float(g_x))
        gyroscope_y.append(float(g_y))
        gyroscope_z.append(float(g_z))
    except Exception:

        pass

plt.plot(acceleration_x)
plt.plot(acceleration_y)
plt.plot(acceleration_z)
plt.plot(gyroscope_x)
plt.plot(gyroscope_y)
plt.plot(gyroscope_z)
plt.xlabel('Time (seconds)')
plt.ylabel('Potentiometer Reading')
plt.title('Potentiometer Reading vs. Time')
plt.show()

ser.close()
