from PyQt5 import QtCore, QtWidgets
import threading
import datetime
import pandas as pd

# Load UI
from ui.Ui_main_window import Ui_MainWindow

# LoadView
from views.SensorView import SensorOptionsDialog
from views.ProfileView import ProfileOptionsDialog
from views.ErrorView import ErrorView
from views.About import AboutThisAppDialog
from views.HistoryView import HistoryViewDialog

# import modules
import utils.sensor
from utils.sensor import (
    getSensorData,
    importRawData,
    stopGetData,
    queue,
    q_ax,
    q_ay,
    q_az,
)

from utils.CNN import importCnnModel, process_raw_data
import utils.CNN

# database
from database.PunchingBag import PunchingBag
from models.SensorModel import Sensor
from models.CnnModel import CnnModel

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
        self.ui.history_button.clicked.connect(self.history_button_pressed)

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
        self.update_punch_data_timer.setInterval(1000)
        self.update_punch_data_timer.timeout.connect(self.update_punches_view)

        # UI
        self.ui.save_folder_line.setText("boxing-gui/Profies/User/")

        # Create model
        self.sensor = Sensor()

    def start_button_pressed(self):
        # clear plot chart
        self.ui.acceleration_chart.clear()

        # Wait for import model to finish
        self.load_model_thread.join()

        self.update_punch_data_timer.start()

        try:
            getSensorData(self.sensor.port, self.sensor.baudrate)
            # self.sensor.getData()

            # store sensor's data to queue
            self.get_data_thread = threading.Thread(target=importRawData)
            self.get_data_thread.start()
            print("Started get data thread")

            # Get data from queue to process
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
            ErrorView().dlg_deviceNotFound("Device not Found!\nSetup device in Options")

    def average(self, list) -> str:
        # return str(sum(list) / len(list))
        return str("{:.0f}".format(sum(list) / len(list)))

    def update_punches_view(self):
        global total_punches
        total_punches = utils.CNN.total_p_value
        self.ui.number_of_punches.setText(str(utils.CNN.count))
        self.ui.current_force_line.setText(str("{:.0f}".format(utils.CNN.p_value)))
        self.ui.peak_force_line.setText(str("{:.0f}".format(max(total_punches))))
        self.ui.average_force_line.setText(self.average(total_punches))

        # self.ui.history_table
        self.ui.history_table.clear()
        for value in total_punches:
            self.ui.history_table.insertItem(0, str("{:.0f} N".format(value)))

        # Plot Acel
        self.ui.acceleration_chart.clear()

        # update 3 valie ax, ay, az
        self.ui.acceleration_chart.plot(
            range(0, len(list(q_ax.queue))),
            list(q_ax.queue),
            pen={"color": "r", "width": 1},
            name="ax",
        )

        self.ui.acceleration_chart.plot(
            range(0, len(list(q_ay.queue))),
            list(q_ay.queue),
            pen={"color": "g", "width": 1},
            name="ay",
        )

        self.ui.acceleration_chart.plot(
            range(0, len(list(q_az.queue))),
            list(q_az.queue),
            pen={"color": "b", "width": 1},
            name="az",
        )

    def stop_button_pressed(self):
        global total_punches

        # Cancel all threads
        stopGetData()
        # stop timer update main view
        self.update_punch_data_timer.stop()
        

        self.ui.start_button.setEnabled(True)
        self.ui.stop_button.setEnabled(False)
        self.ui.zero_button.setEnabled(True)

        # Wait for using all data in queue
        self.get_data_thread.join()
        # self.process_raw_data_thread.join()
        
        # Save history data
        if self.ui.log_check.isChecked():
            path = self.ui.save_folder_line.text()
            # filename: dd-mm-YYYY hh:mm:ss
            name_format = datetime.datetime.now().strftime("%x %X").replace("/", "-")
            name_format = name_format.replace(":", "-")
            filename = name_format + ".xlsx"
            filename = "yes_no_punches " + filename
            # print(f"save file to {filename}")
            total_punches.pop(0)
            total_punches = pd.DataFrame(total_punches)

            utils.CNN.df1.to_excel(path + filename, index=False)
            total_punches.to_excel(
                path + "Force_model_" + name_format + ".xlsx",
                index=False,
                header=["f(model)"],
            )

    def zero_button_pressed(self):
        self.reset_plots()

        self.ui.zero_button.setEnabled(False)

    def history_button_pressed(self):
        historyView = HistoryViewDialog(self)
        historyView.exec_()
        
    # LOAD MENU FILES
    def option_button_pressed(self, signal):
        # Load sensor option ui
        dlg = SensorOptionsDialog(self, self.sensor)
        dlg.exec_()

    def profileOptionsTriggered(self, signal):
        dlg = ProfileOptionsDialog(self)
        # TODO: LOAD FROM DATABASE AUTH
        (
            # _,
            name,
            age,
            user_height,
            user_weight,
            user_metric,
            # _,
            # _,
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
