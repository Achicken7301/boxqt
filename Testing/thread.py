import time

from PyQt5.QtCore import pyqtSlot, QThreadPool, QTimer
from PyQt5.QtWidgets import (
    QLabel,
    QWidget,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QApplication,
)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        # self.threadpool = QThreadPool()
        # print("Multithreading with maximum %d threads" % self.
        # threadpool.maxThreadCount())

        self.setFixedSize(250, 100)
        self.setWindowTitle("Sheep Picker")

        self.sheep_number = 1
        self.timer = QTimer()
        self.picked_sheep_label = QLabel()
        self.counted_sheep_label = QLabel()

        self.layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.thread_manager = QThreadPool()
        self.pick_sheep_button = QPushButton("Pick a sheep!")

        self.layout.addWidget(self.counted_sheep_label)
        self.layout.addWidget(self.pick_sheep_button)
        self.layout.addWidget(self.picked_sheep_label)

        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

        self.timer.timeout.connect(self.count_sheep)
        self.pick_sheep_button.pressed.connect(self.pick_sheep_safely)

        self.timer.start()

    @pyqtSlot()
    def count_sheep(self):
        self.sheep_number += 1
        self.counted_sheep_label.setText(f"Counted {self.sheep_number} sheep.")

    @pyqtSlot()
    def pick_sheep(self):
        self.picked_sheep_label.setText(f"Sheep {self.sheep_number} picked!")
        time.sleep(5)  # This function doesn't affect GUI responsiveness anymore...

    @pyqtSlot()
    def pick_sheep_safely(self):
        self.thread_manager.start(self.pick_sheep)  # ...since .start() is used!


if __name__ == "__main__":
    app = QApplication([])

    main_window = MainWindow()
    main_window.show()

    app.exec()