# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\laragon\www\boxqt\boxing-gui\ui\sensor_option.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SensorOptions(object):
    def setupUi(self, SensorOptions):
        SensorOptions.setObjectName("SensorOptions")
        SensorOptions.resize(420, 177)
        self.gridLayout = QtWidgets.QGridLayout(SensorOptions)
        self.gridLayout.setObjectName("gridLayout")
        self.clear_bluetooth_devices_btn = QtWidgets.QPushButton(SensorOptions)
        self.clear_bluetooth_devices_btn.setObjectName("clear_bluetooth_devices_btn")
        self.gridLayout.addWidget(self.clear_bluetooth_devices_btn, 2, 2, 1, 1)
        self.baudrate = QtWidgets.QLineEdit(SensorOptions)
        self.baudrate.setObjectName("baudrate")
        self.gridLayout.addWidget(self.baudrate, 1, 2, 1, 2)
        self.scan_bluetooth_devices_btn = QtWidgets.QPushButton(SensorOptions)
        self.scan_bluetooth_devices_btn.setObjectName("scan_bluetooth_devices_btn")
        self.gridLayout.addWidget(self.scan_bluetooth_devices_btn, 2, 1, 1, 1)
        self.list_bluetooth_ports = QtWidgets.QListWidget(SensorOptions)
        self.list_bluetooth_ports.setObjectName("list_bluetooth_ports")
        self.gridLayout.addWidget(self.list_bluetooth_ports, 0, 1, 1, 3)
        self.label = QtWidgets.QLabel(SensorOptions)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.sensorOptionButtonBox = QtWidgets.QDialogButtonBox(SensorOptions)
        self.sensorOptionButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.sensorOptionButtonBox.setObjectName("sensorOptionButtonBox")
        self.gridLayout.addWidget(self.sensorOptionButtonBox, 2, 3, 1, 1)

        self.retranslateUi(SensorOptions)
        self.sensorOptionButtonBox.accepted.connect(SensorOptions.accept) # type: ignore
        self.sensorOptionButtonBox.rejected.connect(SensorOptions.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SensorOptions)

    def retranslateUi(self, SensorOptions):
        _translate = QtCore.QCoreApplication.translate
        SensorOptions.setWindowTitle(_translate("SensorOptions", "Device Options"))
        self.clear_bluetooth_devices_btn.setText(_translate("SensorOptions", "Clear"))
        self.baudrate.setText(_translate("SensorOptions", "115200"))
        self.scan_bluetooth_devices_btn.setText(_translate("SensorOptions", "Scan for Device"))
        self.label.setText(_translate("SensorOptions", "Baudrate:"))