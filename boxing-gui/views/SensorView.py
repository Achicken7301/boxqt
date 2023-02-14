from PyQt5 import QtWidgets
# Load UI file
from ui.Ui_sensor_option import Ui_SensorOptions

# Import modules
from utils.bluetooth import serial_ports
import utils.sensor

# Imports View
from views.ErrorView import dlg_deviceNotFound

class SensorOptionsDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SensorOptions()
        self.ui.setupUi(self)

        # Button
        self.ui.scan_bluetooth_devices_btn.clicked.connect(self.bluetoothScan)
        self.ui.clear_bluetooth_devices_btn.clicked.connect(self.clearListPorts)

        # self.ui.submit.clicked.connect(self.submitClose)
        self.ui.sensorOptionButtonBox.accepted.connect(self.submitClose)
        self.ui.sensorOptionButtonBox.rejected.connect(self.rejected)

        # AUTO Scan Bluetooth
        self.bluetoothScan()
        self.ui.list_bluetooth_ports.itemDoubleClicked.connect(
            self.itemDoubleClicked_event
        )

    def submitClose(self):
        # pass data to MainWindow
        utils.sensor.baudrate = self.ui.baudrate.text()
        print(f"{utils.sensor.port} is selected")
        print(f"Baudrate {utils.sensor.baudrate} is selected")
        self.accept()

    def bluetoothScan(self):
        self.clearListPorts()

        list_ports = serial_ports()
        if len(list_ports) == 0:
            dlg_deviceNotFound("Device NOT found!!!\nPlease connect to device via Bluetooth")
            
        self.ui.list_bluetooth_ports.addItems(list_ports)
        self.ui.list_bluetooth_ports.itemClicked.connect(self.itemClicked_event)

    def itemDoubleClicked_event(self, item):
        utils.sensor.port = item.text()
        self.submitClose()

    def itemClicked_event(self, item):
        utils.sensor.port = item.text()

    def clearListPorts(self):
        self.ui.list_bluetooth_ports.clear()
