from PyQt5 import QtWidgets, uic, QtCore, QtGui
import sys
import serial
import datetime
import serial.tools.list_ports
import pandas as pd
import os
import shutil


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.port = "COM3"
        self.baudrate = 115200
        self.is_record = False
        uic.loadUi("src/ui/DevMainWindow.ui", self)

        self.my_widget.addLegend()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.my_widget.setProperty("backgroundBrush", brush)

        # Load the UI Page
        self.portScan()
        self.startRecordBtn.clicked.connect(self.startRecord)
        self.stopRecordBtn.clicked.connect(self.stopRecord)
        self.uiPortScan.clicked.connect(self.portScan)
        self.deleteFile.clicked.connect(self.deleteBtn)
        self.moveFile.clicked.connect(self.moveFileBtn)

        # Timer
        self.recordDataTimer = QtCore.QTimer()
        self.recordDataTimer.timeout.connect(lambda: self.recordData())

        # Dir path
        self.filePath = "data/"
        self.dir.setText(self.filePath)

    def moveFileBtn(self):
        self.toDirectory = self.dir.text()
        self.dir.setText(self.toDirectory)
        shutil.move(self.filename, self.toDirectory)
        self.status.setText(
            f"Moved file {self.filename} to {self.toDirectory} successfully"
        )
        print(f"Moved file {self.filename} to {self.toDirectory} successfully")

    def deleteBtn(self):
        os.remove(self.filename)
        self.status.setText(f"Deleted file {self.filename} succesfully")
        print(f"Deleted file {self.filename} succesfully")

    def clearList(self):
        print("clear list")
        self.portOnHand.clear()

    def startRecord(self):
        self.status.clear()
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

            self.startRecordBtn.setEnabled(False)
            self.stopRecordBtn.setEnabled(True)

            # TimerRun
            self.recordDataTimer.start()  # Interupt every 1ms = 1000Hz

    def stopRecord(self):
        if self.is_record == True:

            self.startRecordBtn.setEnabled(True)
            self.stopRecordBtn.setEnabled(False)

            self.is_record = False
            self.ser.close()
            self.recordDataTimer.stop()
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
        self.filename = "AcelGyro " + self.filename
        # clean data
        ax_buffer = []
        ay_buffer = []
        az_buffer = []
        gx_buffer = []
        gy_buffer = []
        gz_buffer = []
        for i in range(len(self.data)):
            try:
                ax, ay, az, gx, gy, gz = self.data[i][0].split(",")
                ax_buffer.append(float(ax))
                ay_buffer.append(float(ay))
                az_buffer.append(float(az))
                gx_buffer.append(float(gx))
                gy_buffer.append(float(gy))
                gz_buffer.append(float(gz))
            except Exception as e:
                print(e)

        # plot data: x, y values
        self.my_widget.clear()

        self.my_widget.plot(
            range(0, len(list(ax_buffer))),
            list(ax_buffer),
            pen={"color": "r", "width": 1},
        )

        self.my_widget.plot(
            range(0, len(list(ay_buffer))),
            list(ay_buffer),
            pen={"color": "b", "width": 1},
        )

        self.my_widget.plot(
            range(0, len(list(ax_buffer))),
            list(az_buffer),
            pen={"color": "b", "width": 1},
        )

        df = pd.DataFrame()

        df["ax"] = pd.DataFrame(ax_buffer)
        df["ay"] = pd.DataFrame(ay_buffer)
        df["az"] = pd.DataFrame(az_buffer)
        df["gx"] = pd.DataFrame(gx_buffer)
        df["gy"] = pd.DataFrame(gy_buffer)
        df["gz"] = pd.DataFrame(gz_buffer)

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
    def serial_ports(self) -> list:
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


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.setWindowTitle("Aceleration & Gyroscope Device")
    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
