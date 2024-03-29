# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\laragon\www\boxqt\Testing\Bluetooth Scanner Example\device.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeviceDiscovery(object):
    def setupUi(self, DeviceDiscovery):
        DeviceDiscovery.setObjectName("DeviceDiscovery")
        DeviceDiscovery.resize(400, 411)
        self.verticalLayout = QtWidgets.QVBoxLayout(DeviceDiscovery)
        self.verticalLayout.setObjectName("verticalLayout")
        self.list = QtWidgets.QListWidget(DeviceDiscovery)
        self.list.setObjectName("list")
        self.verticalLayout.addWidget(self.list)
        self.groupBox = QtWidgets.QGroupBox(DeviceDiscovery)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.power = QtWidgets.QCheckBox(self.groupBox)
        self.power.setChecked(True)
        self.power.setObjectName("power")
        self.horizontalLayout_2.addWidget(self.power)
        self.discoverable = QtWidgets.QCheckBox(self.groupBox)
        self.discoverable.setChecked(True)
        self.discoverable.setObjectName("discoverable")
        self.horizontalLayout_2.addWidget(self.discoverable)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scan = QtWidgets.QPushButton(DeviceDiscovery)
        self.scan.setObjectName("scan")
        self.horizontalLayout.addWidget(self.scan)
        self.clear = QtWidgets.QPushButton(DeviceDiscovery)
        self.clear.setObjectName("clear")
        self.horizontalLayout.addWidget(self.clear)
        self.quit = QtWidgets.QPushButton(DeviceDiscovery)
        self.quit.setObjectName("quit")
        self.horizontalLayout.addWidget(self.quit)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DeviceDiscovery)
        self.quit.clicked.connect(DeviceDiscovery.accept) # type: ignore
        self.clear.clicked.connect(self.list.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DeviceDiscovery)

    def retranslateUi(self, DeviceDiscovery):
        _translate = QtCore.QCoreApplication.translate
        DeviceDiscovery.setWindowTitle(_translate("DeviceDiscovery", "Bluetooth Scanner"))
        self.groupBox.setTitle(_translate("DeviceDiscovery", "Local Device"))
        self.power.setText(_translate("DeviceDiscovery", "Bluetooth Powered On"))
        self.discoverable.setText(_translate("DeviceDiscovery", "Discoverable"))
        self.scan.setText(_translate("DeviceDiscovery", "Scan"))
        self.clear.setText(_translate("DeviceDiscovery", "Clear"))
        self.quit.setText(_translate("DeviceDiscovery", "Quit"))
