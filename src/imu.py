# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 08:49:14 2022

@author: banhb
"""
import matplotlib.pyplot as plt
import serial
import time
from PyQt5.QtWidgets import*

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure


class Imu:

    def update_accel_x(self):
    
        self.acceleration.x = self.x[1:]  # Remove the first y element.
        # Add a new value 1 higher than the last.
        self.acceleration.x.append(self.x[-1] + 1)

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

        # Update the data.
        self.data_line_accel_x.setData(self.x, self.accel_x)

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
            self.accel_y.append(float(a_y))  # Add a new random value.
        except Exception:
            pass

        # Update the data.
        self.data_line_accel_y.setData(self.x, self.accel_y)

    def update_accel_z(self):

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
            self.accel_z = self.accel_z[1:]  # Remove the first
            self.accel_z.append(float(a_z))  # Add a new random value.
        except Exception:
            pass

        # Update the data.
        self.data_line_accel_z.setData(self.x, self.accel_z)
