# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QDialog
from PyQt5.QtBluetooth import (QBluetoothAddress, QBluetoothServiceInfo,
                                 QBluetoothServiceDiscoveryAgent, QBluetoothLocalDevice)

from Ui_service import Ui_ServiceDiscovery


class ServiceDiscoveryDialog(QDialog):
    def __init__(self, name, address, parent=None):
        super().__init__(parent)
        self._ui = Ui_ServiceDiscovery()
        self._ui.setupUi(self)

        # Using default Bluetooth adapter
        local_device = QBluetoothLocalDevice()
        adapter_address = QBluetoothAddress(local_device.address())

        # In case of multiple Bluetooth adapters it is possible to
        # set which adapter will be used by providing MAC Address.
        # Example code:
        #
        # adapterAddress = QBluetoothAddress("XX:XX:XX:XX:XX:XX")
        # discoveryAgent = QBluetoothServiceDiscoveryAgent(adapterAddress)

        self._discovery_agent = QBluetoothServiceDiscoveryAgent(adapter_address)
        self._discovery_agent.setRemoteAddress(address)

        self.setWindowTitle(name)

        self._discovery_agent.serviceDiscovered.connect(self.add_service)
        self._discovery_agent.finished.connect(self._ui.status.hide)
        self._discovery_agent.start()

    @pyqtSlot(QBluetoothServiceInfo)
    def add_service(self, info):
        line = info.serviceName()
        if not line:
            return

        if info.serviceDescription():
            line += "\n\t" + info.serviceDescription()
        if info.serviceProvider():
            line += "\n\t" + info.serviceProvider()
        print(line)
        self._ui.list.addItem(line)