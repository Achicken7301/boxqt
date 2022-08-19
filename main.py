from PyQt5 import QtWidgets, uic, QtCore
import sys
import serial
import datetime
import csv
import serial.tools.list_ports


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.port_on_hand = None
        self.port_on_bag = None
        self.is_record = False
        # Load the UI Page
        uic.loadUi("src/ui/DevMainWindow.ui", self)
        # self.portScan()
        self.startRecordBtn.clicked.connect(self.startRecord)
        self.stopRecordBtn.clicked.connect(self.stopRecord)
        self.uiPortScan.clicked.connect(self.portScan)
        self.clearListBtn.clicked.connect(self.clearList)

    def clearList(self):
        print("clear list")
        self.portOnHand.clear()
        self.portOnBag.clear()

    def startRecord(self):
        if self.is_record == True:
            print("Already Recording")
        else:
            print("Set is_record to True")
            self.is_record = True
            print("Connect port ser on hand")
            self.ser_on_hand = serial.Serial(port=self.port_on_hand)
            print("Connect port ser on bag")
            self.ser_on_bag = serial.Serial(port=self.port_on_bag)
            self.sample_rate.setText("Recording")
            self.data_on_bag = []
            self.data_on_hand = []
            print("Start Recording")

            # ... init continued ...
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(lambda: self.recordData())
            self.timer.start()

    def stopRecord(self):
        if self.is_record == True:
            self.is_record = False
            self.ser_on_hand.close()
            self.ser_on_bag.close()
            self.sample_rate.setText("Stop")
            print("Stop Recording")
            # Empty data before record a new one
            self.export_to_csv()
            self.data_on_bag = []
            self.data_on_hand = []
        else:
            print("Haven't record anything yet")

    def recordData(self):
        if self.is_record == True:
            try:
                data_ser_on_bag = self.ser_on_bag.readline()
                data_ser_on_bag = data_ser_on_bag.decode().splitlines()

                data_ser_on_hand = self.ser_on_hand.readline()
                data_ser_on_hand = data_ser_on_hand.decode().splitlines()

                self.data_on_bag.append(data_ser_on_hand)
                self.data_on_hand.append(data_ser_on_bag)
            except Exception as e:
                print(e)

    def export_to_csv(self):
        # filename: dd-mm-YYYY hh:mm:ss
        name_format = datetime.datetime.now().strftime("%x %X").replace(
            "/", "-")
        name_format = name_format.replace(":", "-")
        filename = name_format + ".csv"

        with open("Hand " + filename, "w", encoding="UTF8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["a_x,a_y,a_z,f"])
            # write multiple rows
            writer.writerows(self.data_on_bag)

        with open("Bag " + filename, "w", encoding="UTF8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["a_x,a_y,a_z,g_x,g_y,g_z"])
            # write multiple rows
            writer.writerows(self.data_on_hand)

    def portScan(self):
        print("Start scaning")
        r = self.serial_ports()
        print(r)
        if len(r):
            self.portOnHand.clear()
            self.portOnBag.clear()
            self.portOnHand.addItems(r)
            self.portOnBag.addItems(r)
            self.portOnHand.currentTextChanged.connect(self.portOnHandChange)
            self.portOnBag.currentTextChanged.connect(self.portOnBagChange)
            self.port_on_bag = self.portOnHand.currentText()
            self.port_on_hand = self.portOnHand.currentText()
            print("Scanning completeted")
        else:
            print("No ports available")

    def portOnHandChange(self):
        self.port_on_bag = self.portOnHand.currentText()

    def portOnBagChange(self):
        self.port_on_hand = self.portOnHand.currentText()

    # https://stackoverflow.com/questions/55816358/how-to-obtain-bluetooth-port-direction-with-pyserial
    def serial_ports(self):
        port = []
        cp = serial.tools.list_ports.comports()
        for p in cp:
            if "BTHENUM" in p.hwid:
                start_of_address = p.hwid.rfind("&")
                end_of_address = p.hwid.rfind("_")
                address = p.hwid[start_of_address + 1:end_of_address]
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
    main.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
