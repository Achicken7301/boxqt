from PyQt5 import QtWidgets, uic
import sys

# import pyqtgraph as pg
import serial
import datetime
import csv
from PyQt5 import QtWidgets, QtCore

header = ["force", "a_x", "a_y", "a_z", "g_x", "g_y", "g_z"]
port = "COM6"
ser = serial.Serial(port=port, baudrate=115200)
data = []
for _ in range(3):
    try:
        b = ser.readline()
        string_n = b.decode().splitlines()
        data.append(string_n)
        # print(string_n)
        # print(len(string_n))
    except Exception as e:
        raise e


print(type(data[1]))
print(data[1])

with open("filename.csv", "w", encoding="UTF8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    # write multiple rows
    writer.writerows(data)

ser.close()
