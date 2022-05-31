from operator import is_
from PyQt5 import QtWidgets, uic
import sys
from PyQt5 import QtWidgets, QtCore
from pandas import wide_to_long
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint
import serial
import datetime
import csv

ser = serial.Serial(port='COM6', baudrate=115200)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.is_record = False
        self.acceleration_x = []
        self.acceleration_y = []
        self.acceleration_z = []
        self.gyroscope_x = []
        self.gyroscope_y = []
        self.gyroscope_z = []
        self.data = []

        # Load the UI Page
        uic.loadUi('src/ui/main.ui', self)

        length = 500

        self.x = list(range(length))
        self.accel_x = [0 for _ in range(length)]
        self.accel_y = [0 for _ in range(length)]
        self.accel_z = [0 for _ in range(length)]
        self.gyro_x = [0 for _ in range(length)]
        self.gyro_y = [0 for _ in range(length)]
        self.gyro_z = [0 for _ in range(length)]

        self.acceleration.setBackground('w')
        self.gyroscope.setBackground('w')

        # Add legend (line name)
        self.acceleration.addLegend()
        self.gyroscope.addLegend()

        # Add Title
        self.acceleration.setTitle("Acceleration", color="b", size="20pt")
        self.gyroscope.setTitle("Gyroscope", color="b", size="20pt")

        width = 1
        pen_accel_x = pg.mkPen('r', width=width)
        pen_accel_y = pg.mkPen('b', width=width)
        pen_accel_z = pg.mkPen('g', width=width)
        pen_gyro_x = pg.mkPen('c', width=width)
        pen_gyro_y = pg.mkPen('m', width=width)
        pen_gyro_z = pg.mkPen('k', width=width)

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

        # button
        self.startRecordBtn.clicked.connect(lambda: self.start_record())
        self.stopRecordBtn.clicked.connect(lambda: self.stop_record())

        # ... init continued ...
        self.timer = QtCore.QTimer()

        # Update value to plot
        # self.timer.timeout.connect(lambda: self.update_data_imu_on_bag())

        # Recording data
        self.timer.timeout.connect(lambda: self.record_data())

        self.timer.start()

    def start_record(self):
        self.sample_rate.setText("Recording")
        if self.is_record == True:
            print("Already Recording")
        else:
            print("Start Recording")
            self.is_record = True

    def stop_record(self):
        self.export_to_csv()
        self.sample_rate.setText("Stop Recording")
        print("Stop Recording")
        # Empty data before record a new one
        self.is_record = False
        self.acceleration_x = []
        self.acceleration_y = []
        self.acceleration_z = []
        self.gyroscope_x = []
        self.gyroscope_y = []
        self.gyroscope_z = []
        self.data = []

    def record_data(self):
        if self.is_record == True:
            b = ser.readline()
            try:
                string_n = b.decode()
                [a_x, a_y, a_z, g_x, g_y, g_z] = string_n.split()
                print(a_x + " " + a_y + " " + a_z +
                      " " + g_x + " " + g_y + " " + g_z)

                self.acceleration_x.append(float(a_x))
                self.acceleration_y.append(float(a_y))
                self.acceleration_z.append(float(a_z))
                self.gyroscope_x.append(float(g_x))
                self.gyroscope_y.append(float(g_y))
                self.gyroscope_z.append(float(g_z))
            except Exception:
                pass
        else:
            pass

    def export_to_csv(self):
        # import rows to columns
        # https://stackoverflow.com/questions/4155106/python-csv-write-by-column-rather-than-row
        l = [
            self.acceleration_x,
            self.acceleration_y,
            self.acceleration_z,
            self.gyroscope_x,
            self.gyroscope_y,
            self.gyroscope_z,
        ]
        data = zip(*l)

        header = ['a_x', 'a_y', 'a_z', 'g_x', 'g_y', 'g_z']

        # filename: dd-mm-YYYY hh:mm:ss
        name_format = datetime.datetime.now().strftime("%x %X").replace("/", "-")
        name_format = name_format.replace(':', "-")
        filename = name_format + ".csv"

        with open(filename, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(header)

            # write multiple rows
            writer.writerows(data)

    def update_data_imu_on_bag(self):
        self.acceleration.x = self.x[1:]  # Remove the first y element.
        # Add a new value 1 higher than the last.
        self.acceleration.x.append(self.x[-1] + 1)
        b = ser.readline()
        # Cannot decode the 1st value b'\xb4j7\r\n'
        # solve this with try except
        try:
            string_n = b.decode()
            [a_x, a_y, a_z, g_x, g_y, g_z] = string_n.split()
            # print(a_x + " " + a_y + " " + a_z +
            #       " " + g_x + " " + g_y + " " + g_z)
            # Acceleration
            self.accel_x = self.accel_x[1:]
            self.accel_y = self.accel_y[1:]
            self.accel_z = self.accel_z[1:]
            self.accel_x.append(float(a_x))
            self.accel_y.append(float(a_y))
            self.accel_z.append(float(a_z))
            # Gyroscope
            self.gyro_x = self.gyro_x[1:]
            self.gyro_y = self.gyro_y[1:]
            self.gyro_z = self.gyro_z[1:]
            self.gyro_x.append(float(g_x))
            self.gyro_y.append(float(g_y))
            self.gyro_z.append(float(g_z))
        except Exception:
            pass

        # Update the data.
        self.data_line_accel_x.setData(self.x, self.accel_x)
        self.data_line_accel_y.setData(self.x, self.accel_y)
        self.data_line_accel_z.setData(self.x, self.accel_z)
        self.data_line_gyro_x.setData(self.x, self.gyro_x)
        self.data_line_gyro_y.setData(self.x, self.gyro_y)
        self.data_line_gyro_z.setData(self.x, self.gyro_z)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
