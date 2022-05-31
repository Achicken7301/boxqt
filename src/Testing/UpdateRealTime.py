from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.x = list(range(100))  # 100 time points
        self.y = [randint(0, 100) for _ in range(100)]  # 100 data points
        self.a = [randint(0, 100) for _ in range(100)]  # 100 data points
        self.b = [randint(0, 100) for _ in range(100)]  # 100 data points
        self.c = [randint(0, 100) for _ in range(100)]  # 100 data points
        self.d = [randint(0, 100) for _ in range(100)]  # 100 data points

        self.graphWidget.setBackground('w')
        width = 1
        pen = pg.mkPen(color=(255, 0, 0))
        pen_a = pg.mkPen('b', width=width)
        pen_b = pg.mkPen('g', width=width)
        pen_c = pg.mkPen(color=(255, 0, 0))
        pen_d = pg.mkPen(color=(255, 0, 0))
        self.data_line = self.graphWidget.plot(self.x, self.y, pen=pen)
        self.data_line_a = self.graphWidget.plot(self.x, self.y, pen=pen_a)
        self.data_line_b = self.graphWidget.plot(self.x, self.y, pen=pen_b)
        self.data_line_c = self.graphWidget.plot(self.x, self.y, pen=pen_c)
        self.data_line_d = self.graphWidget.plot(self.x, self.y, pen=pen_d)

        # ... init continued ...
        self.timer = QtCore.QTimer()
        # self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):

        self.x = self.x[1:]  # Remove the first y element.
        # Add a new value 1 higher than the last.
        self.x.append(self.x[-1] + 1)

        self.y = self.y[1:]  # Remove the first
        self.a = self.a[1:]  # Remove the first
        self.b = self.b[1:]  # Remove the first
        self.c = self.c[1:]  # Remove the first
        self.d = self.d[1:]  # Remove the first
        self.y.append(randint(0, 100))  # Add a new random value.
        self.a.append(randint(0, 100))  # Add a new random value.
        self.b.append(randint(0, 100))  # Add a new random value.
        self.c.append(randint(0, 100))  # Add a new random value.
        self.d.append(randint(0, 100))  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data.
        self.data_line_a.setData(self.x, self.a)  # Update the data.
        self.data_line_b.setData(self.x, self.b)  # Update the data.
        self.data_line_c.setData(self.x, self.c)  # Update the data.
        self.data_line_d.setData(self.x, self.d)  # Update the data.


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
