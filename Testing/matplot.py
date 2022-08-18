from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from matplotlib.backends.backend_qt5agg import (
    NavigationToolbar2QT as NavigationToolbar)

import numpy as np
import random
import MainWindow

class MplWidget (QWidget):
     
    def __init__(self,  parent=None):

        QWidget . __init__(self,  parent)

        self . canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout . addWidget(self . canvas)

        self . canvas_axes = self . canvas_figure . add_subplot(111)
        self . setLayout(vertical_layout)


class MatplotlibWidget (QMainWindow):

    def __init__(self):
        QMainWindow . __init__(self)
        loadUi("MainWindow.ui", self)
        self . setWindowTitle("PyQt5 & Matplotlib Example GUI")

        # self . pushButton_generate_random_signal . clicked . connect(
        #     self . update_graph)

        # self . addToolBar(NavigationToolbar(self . MplWidget . canvas,  self))

    def update_graph(self):

        fs = 500
        f = random . randint(1,  100)
        ts = 1 / fs
        length_of_signal = 100
        t = np . linspace(0, 1, length_of_signal)

        cosinus_signal = np . cos(2 * np . pi * f * t)
        sinus_signal = np . sin(2 * np . pi * f * t)

        # self . MplWidget . canvas _ ax _ clear()
        # self . MplWidget . canvas _ ax _ plot(t,  cosinus_signal)
        # self . MplWidget . canvas _ ax _ plot(t,  sinus_signal)
        # self . MplWidget . canvas _ ax _ legend(('cosinus',  'sinus'), loc='upper right')
        # self . MplWidget . canvas _ ax _ set_title('Cosinus - Sinus Signal')
        # self . MplWidget . canvas _ draw()


app = QApplication([])
window = MatplotlibWidget()
window . show()
app . exec_()
