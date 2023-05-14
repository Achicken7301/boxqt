from PyQt5 import QtWidgets, uic, QtCore, QtGui
import sys
import serial
import datetime
import serial.tools.list_ports
import pandas as pd
import os
import shutil

from src.ui.DevMainWindow_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Load the UI Page
        uic.loadUi("src/ui/DevMainWindow.ui", self)
        # self = Ui_MainWindow()
        # self.setupUi(self)

        # self.port = "COM6"
        self.baudrate = 1000 * 1000
        self.is_record = False

        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.my_widget.setProperty("backgroundBrush", brush)

        # init btn
        self.startRecordBtn.setEnabled(True)
        self.stopRecordBtn.setEnabled(False)

        self.portScan()
        self.startRecordBtn.clicked.connect(self.startRecord)
        self.stopRecordBtn.clicked.connect(self.stopRecord)
        self.uiPortScan.clicked.connect(self.portScan)
        self.deleteFile.clicked.connect(self.deleteBtn)
        self.moveFile.clicked.connect(self.moveFileBtn)

    def deleteBtn(self):
        print(self.filePath)
        os.remove(self.filePath)

    def moveFileBtn(self):
        toDirectory = "D:\laragon\www\\boxqt\data\\"
        shutil.move(self.filePath, toDirectory)

    def clearList(self):
        print("clear list")
        self.portOnHand.clear()

    def startRecord(self):
        self.startRecordBtn.setEnabled(False)
        self.stopRecordBtn.setEnabled(True)

        if self.is_record == True:
            print("Already Recording")
        else:
            print("Set is_record to True")
            self.is_record = True

            print("Connect port ser on hand")
            self.ser = serial.Serial(port=self.port, baudrate=self.baudrate)
            self.data = []

            self.sample_rate.setText("Recording")
            print("Start Recording")

            # ... init continued ...
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(lambda: self.recordData())
            self.timer.start()

    def stopRecord(self):
        self.startRecordBtn.setEnabled(True)
        self.stopRecordBtn.setEnabled(False)
        if self.is_record == True:
            self.is_record = False
            self.ser.close()
            self.timer.stop()
            self.sample_rate.setText("Stop")
            print("Stop Recording")
            # Empty data before record a new one
            self.export2csv()
            self.data = []
        else:
            print("Haven't record anything yet")

    def recordData(self):
        if self.is_record == True:
            try:
                data_ser = self.ser.readline()
                data_ser = data_ser.decode().splitlines()
                self.data.append(data_ser)
                # print(data_ser_on_bag)
            except Exception as e:
                print(e)

    def export2csv(self):
        # filename: dd-mm-YYYY hh:mm:ss
        name_format = datetime.datetime.now().strftime("%x %X").replace("/", "-")
        name_format = name_format.replace(":", "-")
        self.filename = name_format + ".xlsx"
        # self.filename = name_format + ".csv"
        self.filename = "Force_loadcell" + self.filename
        self.filePath = "D:\laragon\www\\boxqt\\" + self.filename

        f_buffer = []
        for i in range(len(self.data)):
            try:
                f_buffer.append(float(self.data[i][0]))
            except Exception as e:
                print(e)

        # plot data: x, y values
        self.my_widget.clear()
        # self.my_widget.plot(f_buffer)

        self.my_widget.plot(
            range(0, len(list(f_buffer))),
            list(f_buffer),
            pen={"color": "b", "width": 1},
        )

        # Save data to csv
        # df = pd.DataFrame(list(zip(f_buffer)), columns=["f"])
        # df.to_csv(self.filename)

        # Save data to xlsx
        df = pd.DataFrame(f_buffer)
        df.to_excel(self.filename, index=False)

    def portScan(self):
        print("Start scaning")
        r = self.serial_ports()
        print(r)
        if len(r):
            self.portOnHand.clear()
            self.portOnHand.addItems(r)
            self.portOnHand.currentTextChanged.connect(self.portOnHandChange)
            self.port = self.portOnHand.currentText()
            print("Scanning completeted")
        else:
            print("No ports available")

    def portOnHandChange(self):
        self.port = self.portOnHand.currentText()

    # https://stackoverflow.com/questions/55816358/how-to-obtain-bluetooth-port-direction-with-pyserial
    def serial_ports(self):
        port = []
        cp = serial.tools.list_ports.comports()
        for p in cp:
            if "BTHENUM" in p.hwid:
                start_of_address = p.hwid.rfind("&")
                end_of_address = p.hwid.rfind("_")
                address = p.hwid[start_of_address + 1 : end_of_address]
                if int(address, 16) == 0:
                    port_type = "incoming"
                else:
                    port_type = "outgoing"
                # get Outgoing ports ONLY
                if port_type == "outgoing":
                    port.append(p.name)
        return port


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.setWindowTitle("Loadcell Device")
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
