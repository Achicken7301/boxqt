from PyQt5 import QtGui, QtCore, QtWidgets
import threading
import sys

from ui.main_window import Ui_MainWindow
from ui.about_this_app_dialog import Ui_AboutThisAppDialog

# import modules
import utils.sensor
from utils.sensor import getSensorData, importRawData, SensorOptionsDialog, stopGetData, queue
from utils.CNN import importModel, process_raw_data
from utils.user import ProfileOptionsDialog


class AboutThisAppDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AboutThisAppDialog()
        self.ui.setupUi(self)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # *
        # * Button callback
        # *
        self.ui.start_button.clicked.connect(self.start_button_pressed)
        self.ui.stop_button.clicked.connect(self.stop_button_pressed)
        self.ui.zero_button.clicked.connect(self.zero_button_pressed)
        self.ui.option_button.clicked.connect(self.option_button_pressed)
        self.ui.zoom_button.clicked.connect(self.zoom_button_pressed)

        # *
        # * Menu callback
        # *
        self.ui.action_about_this_app.triggered.connect(
            self.action_about_this_app_triggered)
        self.ui.profile_options.triggered.connect(self.profile_options)

        # Load import CNN model
        self.load_model_thread = threading.Thread(target=importModel)
        self.load_model_thread.start()

        # *
        # * Plot setup
        # *
        self.accel_plot_xrange = 500
        self.accel_plot_ptr = 0
        self.accel_buffer = []
        self.accel_plot = self.ui.acceleration_chart.plot(self.accel_buffer, pen="b")

        self.force_plot_xrange = 500
        self.force_plot_ptr = 0
        self.force_buffer = []
        self.force_plot = self.ui.force_chart.plot(self.force_buffer, pen="r")

        self.reset_plots()

        # update plots
        self.plot_timer = QtCore.QTimer()
        self.plot_timer.setInterval(100)

        def timerEvent():
            self.accel_plot_ptr, self.accel_buffer = self.update_plot(
                self.ui.acceleration_chart,
                self.accel_plot,
                self.accel_plot_ptr,
                self.accel_plot_xrange,
                self.accel_buffer,
                # read_data(),
            )
            self.force_plot_ptr, self.force_buffer = self.update_plot(
                self.ui.force_chart,
                self.force_plot,
                self.force_plot_ptr,
                self.force_plot_xrange,
                self.force_buffer,
                # read_data(),
            )

            # self.plot_timer.start()

    def update_plot(self, chart, plot, plot_ptr, plot_xrange, buffer, data=[]):
        buffer = buffer + data
        plot.setData(buffer)
        if plot_ptr >= plot_xrange:
            chart.setXRange(plot_ptr - (plot_xrange - 1), plot_ptr)
        plot_ptr += len(data)

        return plot_ptr, buffer

    def reset_plots(self):
        self.accel_plot_ptr = 0
        self.accel_buffer = []
        self.force_plot_ptr = 0
        self.force_buffer = []
        self.ui.acceleration_chart.setXRange(0, self.accel_plot_xrange - 1)
        self.ui.force_chart.setXRange(0, self.force_plot_xrange - 1)
        self.accel_plot_ptr, self.accel_buffer = self.update_plot(
            self.ui.acceleration_chart,
            self.accel_plot,
            self.accel_plot_ptr,
            self.accel_plot_xrange,
            self.accel_buffer,
        )
        self.force_plot_ptr, self.force_buffer = self.update_plot(
            self.ui.force_chart,
            self.force_plot,
            self.force_plot_ptr,
            self.force_plot_xrange,
            self.force_buffer,
        )

    def get_data_from_sensor_dialog(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate

    def start_button_pressed(self):
        # self.plot_timer.start()
        '''
        Create new thread for getting data
        TODO Show noti when user not connect to bluetooth device
        '''
        getSensorData(utils.sensor.port, utils.sensor.baudrate)
        self.get_data_thread = threading.Thread(target=importRawData)
        self.get_data_thread.start()
        '''
        Make clean data before put into model to predict
        '''
        self.process_raw_data_thread = threading.Thread(
            target=process_raw_data, args=(queue, ))
        self.process_raw_data_thread.start()

        self.ui.start_button.setEnabled(False)
        self.ui.stop_button.setEnabled(True)
        self.ui.zero_button.setEnabled(False)

    def stop_button_pressed(self):
        # self.plot_timer.stop()
        stopGetData()
        self.get_data_thread.join()

        self.ui.start_button.setEnabled(True)
        self.ui.stop_button.setEnabled(False)
        self.ui.zero_button.setEnabled(True)

    def zero_button_pressed(self):
        self.reset_plots()

        self.ui.zero_button.setEnabled(False)

    def zoom_button_pressed(self):
        self.setWindowTitle("Zoom")

    # LOAD MENU FILES
    def option_button_pressed(self):

        # Load sensor option ui
        dlg = SensorOptionsDialog(self)
        dlg.exec_()

    def profile_options(self, signal):
        dlg = ProfileOptionsDialog(self)
        dlg.exec_()

    def action_about_this_app_triggered(self, signal):
        dlg = AboutThisAppDialog(self)
        dlg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # app theme
    # qss = "boxing-gui/Ubuntu.qss"
    # with open(qss, "r") as fh:
    #     app.setStyleSheet(fh.read())

    # set app icon
    app_icon = QtGui.QIcon()
    app_icon.addFile("boxing-gui/icons/logo.png", QtCore.QSize(64, 64))
    app.setWindowIcon(app_icon)

    # TODO clost all port and shit before exit
    sys.exit(app.exec_())
