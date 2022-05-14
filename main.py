from PyQt5 import QtWidgets, uic
import sys
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

        # Load the UI Page
        uic.loadUi('src/ui/main.ui', self)

        length = 200
        
        self.x = list(range(length))
        self.accel_x = [0 for _ in range(length)]
        self.accel_y = [0 for _ in range(length)]
        self.accel_z = [0 for _ in range(length)]
        self.gyro_x = [0 for _ in range(length)]
        self.gyro_y = [0 for _ in range(length)]
        self.gyro_z = [0 for _ in range(length)]

        self.acceleration.setBackground('w')
        self.gyroscope.setBackground('w')
        #Add legend (line name)
        self.acceleration.addLegend()
        self.gyroscope.addLegend()

        pen_accel_x = pg.mkPen('r', width=3)
        pen_accel_y = pg.mkPen('b', width=3)
        pen_accel_z = pg.mkPen('g', width=3)
        pen_gyro_x = pg.mkPen('r', width=3)
        pen_gyro_y = pg.mkPen('b', width=3)
        pen_gyro_z = pg.mkPen('g', width=3)
        self.data_line_accel_x = self.acceleration.plot(
            self.x, self.accel_x, pen=pen_accel_x, name="accel_x")
        self.data_line_accel_y = self.acceleration.plot(
            self.x, self.accel_y, pen=pen_accel_y, name="accel_y")
        self.data_line_accel_z = self.acceleration.plot(
            self.x, self.accel_z, pen=pen_accel_z, name="accel_z")
        self.data_line_gyro_x = self.gyroscope.plot(
            self.x, self.gyro_x, pen=pen_gyro_x, name="gyro_x")
        self.data_line_gyro_y = self.gyroscope.plot(
            self.x, self.gyro_y, pen=pen_gyro_y, name="gyro_y")
        self.data_line_gyro_z = self.gyroscope.plot(
            self.x, self.gyro_z, pen=pen_gyro_z, name="gyro_z")

        # ... init continued ...
        self.timer = QtCore.QTimer()
        # self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_accel_x)
        self.timer.timeout.connect(self.update_accel_y)
        self.timer.timeout.connect(self.update_accel_z)
        self.timer.timeout.connect(self.update_gyro_x)
        self.timer.timeout.connect(self.update_gyro_y)
        self.timer.timeout.connect(self.update_gyro_z)
        self.timer.start()

    def update_accel_x(self):

        self.acceleration.x = self.x[1:]  # Remove the first y element.
        # Add a new value 1 higher than the last.
        self.acceleration.x.append(self.x[-1] + 1)

        b = ser.readline()
        # Cannot decode the 1st value b'\xb4j7\r\n'
        # solve this with try except
        try:
            self.string_n = b.decode()
            [a_x, a_y, a_z, g_x, g_y, g_z] = string_n.split()
            self.accel_x = self.accel_x[1:]  # Remove the first
            self.accel_x.append(float(a_x))  # Add a new random value.
        except Exception:
            pass

        # Update the data.
        self.data_line_accel_x.setData(self.x, self.accel_x)

    def update_accel_y(self):

        self.acceleration.x = self.x[1:]  # Remove the first y element.
        # Add a new value 1 higher than the last.
        self.acceleration.x.append(self.x[-1] + 1)

        b = ser.readline()
        # Cannot decode the 1st value b'\xb4j7\r\n'
        # solve this with try except
        try:
            string_n = b.decode()
            [a_x, a_y, a_z, g_x, g_y, g_z] = string_n.split()
            self.accel_y = self.accel_y[1:]  # Remove the first
            self.accel_y.append(float(a_y))  # Add a new random value.
        except Exception:
            pass

        # Update the data.
        self.data_line_accel_y.setData(self.x, self.accel_y)

    def update_accel_z(self):

        self.acceleration.x = self.x[1:]  # Remove the first y element.
        # Add a new value 1 higher than the last.
        self.acceleration.x.append(self.x[-1] + 1)

        b = ser.readline()
        # Cannot decode the 1st value b'\xb4j7\r\n'
        # solve this with try except
        try:
            string_n = b.decode()
            [a_x, a_y, a_z, g_x, g_y, g_z] = string_n.split()
            self.accel_z = self.accel_z[1:]  # Remove the first
            self.accel_z.append(float(a_z))  # Add a new random value.
        except Exception:
            pass

        # Update the data.
        self.data_line_accel_z.setData(self.x, self.accel_z)

    def update_gyro_x(self):

        self.gyroscope.x = self.x[1:]  # Remove the first y element.
        # Add a new value 1 higher than the last.
        self.gyroscope.x.append(self.x[-1] + 1)

        b = ser.readline()
        # Cannot decode the 1st value b'\xb4j7\r\n'
        # solve this with try except
        try:
            string_n = b.decode()
            [a_x, a_y, a_z, g_x, g_y, g_z] = string_n.split()
            self.gyro_x = self.gyro_x[1:]  # Remove the first
            self.gyro_x.append(float(g_x))  # Add a new random value.
        except Exception:
            pass

        # Update the data.
        self.data_line_gyro_x.setData(self.x, self.gyro_x)

    def update_gyro_y(self):

        self.gyroscope.x = self.x[1:]  # Remove the first y element.
        # Add a new value 1 higher than the last.
        self.gyroscope.x.append(self.x[-1] + 1)

        b = ser.readline()
        # Cannot decode the 1st value b'\xb4j7\r\n'
        # solve this with try except
        try:
            string_n = b.decode()
            [a_x, a_y, a_z, g_x, g_y, g_z] = string_n.split()
            self.gyro_y = self.gyro_y[1:]  # Remove the first
            self.gyro_y.append(float(g_y))  # Add a new random value.
        except Exception:
            pass

        # Update the data.
        self.data_line_gyro_y.setData(self.x, self.gyro_y)

    def update_gyro_z(self):

        self.gyroscope.x = self.x[1:]  # Remove the first y element.
        # Add a new value 1 higher than the last.
        self.gyroscope.x.append(self.x[-1] + 1)

        b = ser.readline()
        # Cannot decode the 1st value b'\xb4j7\r\n'
        # solve this with try except
        try:
            string_n = b.decode()
            [a_x, a_y, a_z, g_x, g_y, g_z] = string_n.split()
            self.gyro_z = self.gyro_z[1:]  # Remove the first
            self.gyro_z.append(float(g_z))  # Add a new random value.
        except Exception:
            pass

        # Update the data.
        self.data_line_gyro_z.setData(self.x, self.gyro_z)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
