from PyQt5 import QtCore, QtWidgets
import threading
import pandas as pd

# Load UI
from ui.Ui_main_window import Ui_MainWindow

# LoadView
from views.SensorView import SensorOptionsDialog
from views.ProfileView import ProfileOptionsDialog
from views.ErrorView import dlg_deviceNotFound
from views.About import AboutThisAppDialog

# import modules
import utils.sensor
from utils.sensor import (
    getSensorData,
    importRawData,
    stopGetData,
    queue,
)
from utils.CNN import importCnnModel, process_raw_data, window_mask
import utils.CNN

# database
from database.PunchingBag import PunchingBag


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

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
            self.action_about_this_app_triggered
        )
        self.ui.profile_options.triggered.connect(self.profileOptionsTriggered)

        # Load import CNN model
        self.load_model_thread = threading.Thread(target=importCnnModel)
        self.load_model_thread.start()

        # *
        # * Plot setup
        # *
        self.ui.acceleration_chart.addLegend()

        self.update_punch_data_timer = QtCore.QTimer()
        self.update_punch_data_timer.setInterval(100)
        self.update_punch_data_timer.timeout.connect(self.update_punches_view)

    def start_button_pressed(self):

        self.update_punch_data_timer.start()
        try:
            getSensorData(utils.sensor.port, utils.sensor.baudrate)
            self.get_data_thread = threading.Thread(target=importRawData)
            self.get_data_thread.start()
            print("Started get data thread")
            """
            Make clean data before put into model to predict
            """
            self.process_raw_data_thread = threading.Thread(
                target=process_raw_data, args=(queue,)
            )
            self.process_raw_data_thread.start()
            print("Started process raw data thread")

            self.ui.start_button.setEnabled(False)
            self.ui.stop_button.setEnabled(True)
            self.ui.zero_button.setEnabled(False)
        except Exception as e:
            print(e)
            dlg_deviceNotFound("Device not Found!\nSetup device in Options")

    def update_punches_view(self):

        self.ui.number_of_punches.setText(str(utils.CNN.count))
        self.ui.current_force_line.setText(str(utils.CNN.p_value))
        self.ui.peak_force_line.setText(str(max(utils.CNN.total_p_value)))

        # Plot Acel
        if not utils.CNN.acceleration_data_for_view.empty:
            self.ui.acceleration_chart.clear()
            # update 3 valie ax, ay, az
            self.ui.acceleration_chart.plot(
                utils.CNN.acceleration_data_for_view.index,
                utils.CNN.acceleration_data_for_view[0],
                pen={"color": "r", "width": 3},
                name="ax",
            )
            self.ui.acceleration_chart.plot(
                utils.CNN.acceleration_data_for_view.index,
                utils.CNN.acceleration_data_for_view[1],
                pen={"color": "g", "width": 3},
                name="ay",
            )
            self.ui.acceleration_chart.plot(
                utils.CNN.acceleration_data_for_view.index,
                utils.CNN.acceleration_data_for_view[2],
                pen={"color": "b", "width": 3},
                name="az",
            )
            utils.CNN.acceleration_data_for_view = pd.DataFrame()

    def stop_button_pressed(self):
        # self.plot_timer.stop()
        self.update_punch_data_timer.stop()
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
    def option_button_pressed(self, signal):
        # Load sensor option ui
        dlg = SensorOptionsDialog(self)
        if dlg.exec_():
            pass

    def profileOptionsTriggered(self, signal):
        dlg = ProfileOptionsDialog(self)
        # TODO: LOAD FROM DATABASE AUTH
        (
            _,
            name,
            age,
            user_height,
            user_weight,
            user_metric,
            _,
            _,
            hanging_style,
            bag_weight,
            bag_lenght,
            bag_l2top,
            bag_ltbtm,
        ) = PunchingBag().get_user_bag("1")

        # Load to ProfileVIew
        # Radio BTN
        if hanging_style == 0:
            ProfileOptionsDialog.freestanding_radioBtn_checked(dlg)
        else:
            ProfileOptionsDialog.hanging_radioBtn_checked(dlg)

        if user_metric == 0:
            ProfileOptionsDialog.imperial_system_radioBtn_checked(dlg)
        else:
            ProfileOptionsDialog.metric_system_radioBtn_checked(dlg)

        # Punching bag
        dlg.ui.punching_bag_input_length.setText(str(bag_lenght))
        dlg.ui.punching_bag_input_btm2gnd.setText(str(bag_ltbtm))
        dlg.ui.punching_bag_input_height2top.setText(str(bag_l2top))
        dlg.ui.punching_bag_input_weight.setText(str(bag_weight))

        # User
        dlg.ui.user_input_name.setText(str(name))
        dlg.ui.user_input_age.setText(str(age))
        dlg.ui.user_input_height.setText(str(user_height))
        dlg.ui.user_input_weight.setText(str(user_weight))

        if dlg.exec_():
            # SAVE BACK TO DATABASE
            dlg.save_user_setting()
            dlg.save_bag_setting()

    def action_about_this_app_triggered(self, signal):
        dlg = AboutThisAppDialog(self)
        dlg.exec_()