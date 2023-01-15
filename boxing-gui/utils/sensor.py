from ui.sensor_option import Ui_SensorOptions
from PyQt5 import QtWidgets

# import modules
import utils.CNN
from utils.CNN import *
from utils.bluetooth import serial_ports
import serial

global acel_gyro_ser, get_data_flag, queue
get_data_flag = False

ax = []
ay = []
az = []
gx = []
gy = []
gz = []
queue = [ax, ay, az, gx, gy, gz]


def close_ser():
    global acel_gyro_ser
    acel_gyro_ser.close()


def stopGetData():
    global acel_gyro_ser, get_data_flag, process_raw_data_flag

    acel_gyro_ser.close()

    # Condition to Cancel thread
    get_data_flag = True
    utils.CNN.process_raw_data_flag = True


def getSensorData(port: str, baudrate: int = 115200):
    global get_data_flag, acel_gyro_ser, process_raw_data_flag
    
    acel_gyro_ser = serial.Serial(port=port, baudrate=baudrate)

    # Condition to start thread
    get_data_flag = False
    utils.CNN.process_raw_data_flag = False


def importRawData():
    global acel_gyro_ser, get_data_flag
    while 1:
        try:
            # print("Still getting data...")
            b = acel_gyro_ser.readline()
            data_ser = b.decode().splitlines()
            # Store data to window
            ax_ser, ay_ser, az_ser, gx_ser, gy_ser, gz_ser = data_ser[0].split(
                ",")
            queue[0].append(ax_ser)
            queue[1].append(az_ser)
            queue[2].append(ay_ser)
            queue[3].append(gx_ser)
            queue[4].append(gy_ser)
            queue[5].append(gz_ser)
        except Exception as e:
            print(e)
            break


class SensorOptionsDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SensorOptions()
        self.ui.setupUi(self)

        # Button
        self.ui.scan_bluetooth_devices_btn.clicked.connect(self.bluetoothScan)
        self.ui.clear_bluetooth_devices_btn.clicked.connect(
            self.clearListPorts)

        self.ui.submit.clicked.connect(self.submitClose)

        # AUTO Scan Bluetooth
        self.bluetoothScan()
        self.ui.list_bluetooth_ports.itemDoubleClicked.connect(
            self.itemDoubleClicked_event)

    def submitClose(self):
        # pass data to MainWindow
        utils.sensor.baudrate = self.ui.baudrate.text()
        self.accept()

    def bluetoothScan(self):
        self.clearListPorts()

        list_ports = serial_ports()
        self.ui.list_bluetooth_ports.addItems(list_ports)

        self.ui.list_bluetooth_ports.itemClicked.connect(
            self.itemClicked_event)

    def itemDoubleClicked_event(self, item):
        utils.sensor.port = item.text()
        self.submitClose()

    def itemClicked_event(self, item):
        utils.sensor.port = item.text()

    def clearListPorts(self):
        self.ui.list_bluetooth_ports.clear()
