from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint
import serial

ser = serial.Serial(port='COM6', baudrate=115200)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.x = list(range(500))  # 500 time points
        self.accel_x = [0 for _ in range(500)]  # 500 data points
        # self.accel_y = [0 for _ in range(500)]  # 500 data points

        self.graphWidget.setBackground('w')

        pen_accel_x = pg.mkPen(color=(255, 0, 0))
        pen_accel_y = pg.mkPen(color=(0, 255, 0))
        self.data_line_accel_x = self.graphWidget.plot(self.x, self.accel_x, pen=pen_accel_x)
        # self.data_line_accel_y = self.graphWidget.plot(self.x, self.pen_accel_y, pen=pen_accel_y)

        # ... init continued ...
        self.timer = QtCore.QTimer()
        # self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_accel_x)
        self.timer.start()

    def update_accel_x(self):
    
        self.x = self.x[1:]  # Remove the first y element.
        # Add a new value 1 higher than the last.
        self.x.append(self.x[-1] + 1)

        b = ser.readline()
        # Cannot decode the 1st value b'\xb4j7\r\n'
        # solve this with try except
        try:
            string_n = b.decode()

            print(string_n)
            [a_x, a_y, a_z, g_x, g_y, g_z] = string_n.split()
            self.accel_x = self.accel_x[1:]  # Remove the first
            self.accel_x.append(float(a_x))  # Add a new random value.
        except Exception:
            pass

        self.data_line_accel_x.setData(self.x, self.accel_x)  # Update the data.

    def update_accel_y(self):
    
        self.x = self.x[1:]  # Remove the first y element.
        # Add a new value 1 higher than the last.
        self.x.append(self.x[-1] + 1)

        b = ser.readline()
        # Cannot decode the 1st value b'\xb4j7\r\n'
        # solve this with try except
        try:
            string_n = b.decode()

            print(string_n)
            [a_x, a_y, a_z, g_x, g_y, g_z] = string_n.split()
            self.accel_y = self.accel_y[1:]  # Remove the first
            self.accel_y.append(float(a_x))  # Add a new random value.
        except Exception:
            pass

        self.data_line_accel_y.setData(self.x, self.accel_y)  # Update the data.


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
