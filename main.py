from PyQt5 import QtWidgets, uic
import sys
import glob
import serial
import datetime
import csv
import time
from PyQt5 import QtWidgets, QtCore
import concurrent.futures


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.port = None
        self.is_record = False
        # Load the UI Page
        uic.loadUi("src/ui/main.ui", self)
        # self.port_scan()
        self.startRecordBtn.clicked.connect(self.start_record)
        self.stopRecordBtn.clicked.connect(self.stop_record)
        self.portScan.clicked.connect(self.port_scan)
        self.clearListBtn.clicked.connect(self.clearList)

    def clearList(self):
        print("clear list")
        self.listPorts.clear()

    def start_record(self):
        if self.is_record == True:
            print("Already Recording")
        else:
            self.is_record = True
            self.ser = serial.Serial(port=self.port)
            self.sample_rate.setText("Recording")
            self.data = []
            print("Start Recording")

            # ... init continued ...
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(lambda: self.record_data())
            self.timer.start()

    def stop_record(self):
        if self.is_record == True:
            self.is_record = False
            self.ser.close()
            self.sample_rate.setText("Stop")
            print("Stop Recording")
            # Empty data before record a new one
            self.export_to_csv()
            self.data = []
        else:
            print("Haven't record anything yet")

    def record_data(self):
        if self.is_record == True:
            try:
                b = self.ser.readline()
                string_n = b.decode().splitlines()
                self.data.append(string_n)
            except Exception as e:
                print(e)

    def export_to_csv(self):
        header = ["force a_x a_y a_z g_x g_y g_z"]
        # filename: dd-mm-YYYY hh:mm:ss
        name_format = datetime.datetime.now().strftime("%x %X").replace("/", "-")
        name_format = name_format.replace(":", "-")
        filename = name_format + ".csv"

        with open(filename, "w", encoding="UTF8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(header)
            # write multiple rows
            writer.writerows(self.data)

    def port_scan(self):
        self.listPorts.clear()
        print("Start scaning")
        # r = executor.submit(self.serial_ports)
        r = self.serial_ports()
        if len(r):
            self.listPorts.addItems(r)
            print("Scanning completeted")
            self.listPorts.itemClicked.connect(self.getItem)
        else:
            print("No ports available")

    def getItem(self):
        print("Selected port: " + self.listPorts.currentItem().text())
        self.port = self.listPorts.currentItem().text()

    # https://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python
    def serial_ports(self):
        """Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
        """
        if sys.platform.startswith("win"):
            # ports = ['COM%s' % (i + 1) for i in range(256)]
            ports = ["COM%s" % (i + 1) for i in range(8)]
        elif sys.platform.startswith("linux") or sys.platform.startswith("cygwin"):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob("/dev/tty[A-Za-z]*")
        elif sys.platform.startswith("darwin"):
            ports = glob.glob("/dev/tty.*")
        else:
            raise EnvironmentError("Unsupported platform")

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
