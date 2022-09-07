import sys
import glob
import serial


class BluetoothScanner(object):

    def __init__(self, *args):
        super(BluetoothScanner, self).__init__(*args)
        self.portScan(self)

    def portScan(self):
        self.listPorts.clear()
        r = self.serial_ports()
        if len(r):
            self.listPorts.addItems(r)
            self.listPorts.itemClicked.connect(self.getItem)
        else:
            print("No ports available")

    def getItem(self):
        print(self.text())
        port = self.text()
        self.ser = serial.Serial(port=port, baudrate=115200)

    # https://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python
    def serial_ports():
        """ Lists serial port names

            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith(
                'cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result