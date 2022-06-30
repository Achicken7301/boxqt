from PyQt5 import QtWidgets, uic
import sys
import pyqtgraph as pg
import serial
import datetime
import csv
from PyQt5 import QtWidgets, QtCore

ser = serial.Serial(port='COM6', baudrate=921600)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # self.is_record = False
        self.is_record = False
        self.force = []
        self.acceleration_x = []
        self.acceleration_y = []
        self.acceleration_z = []
        self.gyroscope_x = []
        self.gyroscope_y = []
        self.gyroscope_z = []
        self.data = []

        # Load the UI Page
        uic.loadUi('src/ui/main.ui', self)

        # # button
        self.startRecordBtn.clicked.connect(lambda: self.start_record())
        self.stopRecordBtn.clicked.connect(lambda: self.stop_record())

        # ... init continued ...
        self.timer = QtCore.QTimer()
        # Recording data
        self.timer.timeout.connect(lambda: self.record_data())
        # self.timer.timeout.connect(lambda: self.update_data_force_on_bag())
        self.timer.start()

    def start_record(self):
        self.sample_rate.setText("Recording")
        if self.is_record == True:
            print("Already Recording")
        else:
            print("Start Recording")
            self.is_record = True

    def stop_record(self):
        self.export_to_csv()
        self.sample_rate.setText("Stop")
        print("Stop Recording")
        # Empty data before record a new one
        self.is_record = False
        self.acceleration_x = []
        self.acceleration_y = []
        self.acceleration_z = []
        self.gyroscope_x = []
        self.gyroscope_y = []
        self.gyroscope_z = []
        self.data = []

    def record_data(self):
        if self.is_record == True:
            b = ser.readline()
            try:
                string_n = b.decode()
                [force, a_x, a_y, a_z, g_x, g_y, g_z] = string_n.split()
                print(force + ' ' + a_x + ' ' + a_y + ' ' + a_z + ' ' + g_x + ' ' + g_y + ' ' + g_z + ' ')
                self.force.append(float(force))
                self.acceleration_x.append(float(a_x))
                self.acceleration_y.append(float(a_y))
                self.acceleration_z.append(float(a_z))
                self.gyroscope_x.append(float(g_x))
                self.gyroscope_y.append(float(g_y))
                self.gyroscope_z.append(float(g_z))
            except Exception as e:
                print(b)
                print(e)

    def export_to_csv(self):
        # import rows to columns
        # https://stackoverflow.com/questions/4155106/python-csv-write-by-column-rather-than-row
        l = [
            self.force,
            self.acceleration_x,
            self.acceleration_y,
            self.acceleration_z,
            self.gyroscope_x,
            self.gyroscope_y,
            self.gyroscope_z,
        ]
        data = zip(*l)

        header = ['force', 'a_x', 'a_y', 'a_z', 'g_x', 'g_y', 'g_z']

        # filename: dd-mm-YYYY hh:mm:ss
        name_format = datetime.datetime.now().strftime("%x %X").replace("/", "-")
        name_format = name_format.replace(':', "-")
        filename = name_format + ".csv"

        with open(filename, 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            # write multiple rows
            writer.writerows(data)

    def update_data_force_on_bag(self):

        length = 500

        self.x = list(range(length))
        self.force = [0 for _ in range(length)]
        self.force_graph.setBackground('w')

        # # Add legend (line name)
        self.force_graph.addLegend()

        # # Add Title
        self.force_graph.setTitle("Force Graph", color="b", size="10pt")

        width = 1
        pen_force_graph = pg.mkPen('r', width=width)

        self.data_line_force_graph = self.force_graph.plot(
            self.x, self.force, pen=pen_force_graph, name="force")

        self.x = self.x[1:]  # Remove the first y element.
        # Add a new value 1 higher than the last.
        self.x.append(self.x[-1] + 1)
        b = ser.readline()
        # Cannot decode the 1st value b'\xb4j7\r\n'
        # solve this with try except
        try:
            string_n = b.decode()
            print(string_n)
            [force, a_x, a_y, a_z, g_x, g_y, g_z] = string_n.split()
            # Acceleration
            self.force = self.force[1:]
            self.force.append(float(force))
        except Exception as e:
            print(e)
        # Update the data.
        self.data_line_force_graph.setData(self.x, self.force)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
