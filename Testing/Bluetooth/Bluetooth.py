# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

"""PySide6 port of the bluetooth/btscanner example from Qt v6.x"""

import sys

from PyQt5.QtCore import QMetaObject
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtBluetooth import QBluetoothLocalDevice

def bluetoothScaner():
    qt = QBluetoothLocalDevice
    print(qt.allDevices())



if __name__ == '__main__':
    bluetoothScaner()