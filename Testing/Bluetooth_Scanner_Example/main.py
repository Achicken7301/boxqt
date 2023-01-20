import sys

from PyQt5.QtWidgets import QApplication

from device import DeviceDiscoveryDialog


if __name__ == '__main__':
    app = QApplication(sys.argv)
    d = DeviceDiscoveryDialog()
    d.exec()
    sys.exit(0)