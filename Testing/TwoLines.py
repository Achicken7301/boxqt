from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import matplotlib.pyplot as plt
import serial
import time
import pandas as pd


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        # number_of_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        [t, a_x, a_y, a_z, g_x, g_y, g_z] = self.get_data()

        number_of_data = t
        temperature_1 = a_x
        temperature_2 = a_y

        # Add Background colour to white
        self.graphWidget.setBackground('w')
        # Add Title
        self.graphWidget.setTitle("Your Title Here", color="b", size="30pt")
        # Add Axis Labels
        styles = {"color": "#f00", "font-size": "20px"}
        self.graphWidget.setLabel("left", "Temperature (°C)", **styles)
        self.graphWidget.setLabel("bottom", "number_of_data (#)", **styles)
        # Add legend
        self.graphWidget.addLegend()
        # Add grid
        self.graphWidget.showGrid(x=True, y=True)
        # Set Range
        self.graphWidget.setXRange(0, 3000, padding=0)
        self.graphWidget.setYRange(-200, 200, padding=0)

        self.plot(number_of_data, temperature_1, "Sensor1", 'r')
        self.plot(number_of_data, temperature_2, "Sensor2", 'b')

    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        # self.graphWidget.plot(x, y, name=plotname, pen=pen, symbol='+', symbolSize=30, symbolBrush=(color))
        self.graphWidget.plot(x, y, name=plotname,
                              pen=pen, symbolBrush=(color))

    def get_data(*args, **kwargs):
        ser = serial.Serial(port='COM6', baudrate=9600)
        millis = []
        acceleration_x = []
        acceleration_y = []
        acceleration_z = []
        gyroscope_x = []
        gyroscope_y = []
        gyroscope_z = []
        value_quantity = 100
        for i in range(value_quantity):
            b = ser.readline()
            # Cannot decode the 1st value b'\xb4j7\r\n'
            # solved this with try except
            try:
                string_n = b.decode()
                print(string_n)
                [t, a_x, a_y, a_z, g_x, g_y, g_z] = string_n.split()
                millis.append(float(t))
                acceleration_x.append(float(a_x))
                acceleration_y.append(float(a_y))
                acceleration_z.append(float(a_z))
                gyroscope_x.append(float(g_x))
                gyroscope_y.append(float(g_y))
                gyroscope_z.append(float(g_z))
            except Exception:
                pass
        ser.close()
        return millis, acceleration_x, acceleration_y, acceleration_z, gyroscope_x, gyroscope_y, gyroscope_z


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
