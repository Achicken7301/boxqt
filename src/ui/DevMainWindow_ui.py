# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\laragon\www\boxqt\src\ui\DevMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(758, 412)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(10, 10, 10, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.dir = QtWidgets.QLineEdit(self.centralwidget)
        self.dir.setText("")
        self.dir.setObjectName("dir")
        self.gridLayout.addWidget(self.dir, 2, 1, 1, 1)
        self.uiPortScan = QtWidgets.QPushButton(self.centralwidget)
        self.uiPortScan.setObjectName("uiPortScan")
        self.gridLayout.addWidget(self.uiPortScan, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.sample_rate = QtWidgets.QLabel(self.centralwidget)
        self.sample_rate.setObjectName("sample_rate")
        self.gridLayout.addWidget(self.sample_rate, 1, 1, 1, 1)
        self.portOnHand = QtWidgets.QComboBox(self.centralwidget)
        self.portOnHand.setObjectName("portOnHand")
        self.gridLayout.addWidget(self.portOnHand, 0, 1, 1, 1)
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.status, 3, 0, 1, 1)
        self.startRecordBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startRecordBtn.setObjectName("startRecordBtn")
        self.gridLayout.addWidget(self.startRecordBtn, 0, 3, 1, 1)
        self.stopRecordBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopRecordBtn.setObjectName("stopRecordBtn")
        self.gridLayout.addWidget(self.stopRecordBtn, 1, 3, 1, 1)
        self.moveFile = QtWidgets.QPushButton(self.centralwidget)
        self.moveFile.setObjectName("moveFile")
        self.gridLayout.addWidget(self.moveFile, 2, 2, 1, 1)
        self.deleteFile = QtWidgets.QPushButton(self.centralwidget)
        self.deleteFile.setObjectName("deleteFile")
        self.gridLayout.addWidget(self.deleteFile, 2, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.my_widget = PlotWidget(self.centralwidget)
        self.my_widget.setEnabled(False)
        self.my_widget.setAutoFillBackground(True)
        self.my_widget.setObjectName("my_widget")
        self.verticalLayout.addWidget(self.my_widget)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBoard_Setting = QtWidgets.QAction(MainWindow)
        self.actionBoard_Setting.setObjectName("actionBoard_Setting")
        self.action_info = QtWidgets.QAction(MainWindow)
        self.action_info.setObjectName("action_info")
        self.action_About_us = QtWidgets.QAction(MainWindow)
        self.action_About_us.setObjectName("action_About_us")
        self.actionAuto_Congifuration_Wizard = QtWidgets.QAction(MainWindow)
        self.actionAuto_Congifuration_Wizard.setObjectName("actionAuto_Congifuration_Wizard")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionDuplicate = QtWidgets.QAction(MainWindow)
        self.actionDuplicate.setObjectName("actionDuplicate")
        self.actionRename = QtWidgets.QAction(MainWindow)
        self.actionRename.setObjectName("actionRename")
        self.actionRemove = QtWidgets.QAction(MainWindow)
        self.actionRemove.setObjectName("actionRemove")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionProfile1 = QtWidgets.QAction(MainWindow)
        self.actionProfile1.setObjectName("actionProfile1")
        self.actionSetting = QtWidgets.QAction(MainWindow)
        self.actionSetting.setObjectName("actionSetting")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Boxqt for Developers"))
        self.label_2.setText(_translate("MainWindow", "Select port:"))
        self.uiPortScan.setText(_translate("MainWindow", "Scan ports"))
        self.label.setText(_translate("MainWindow", "Recording Status:"))
        self.label_4.setText(_translate("MainWindow", "Directory:"))
        self.sample_rate.setText(_translate("MainWindow", "Suspending"))
        self.status.setText(_translate("MainWindow", "Status"))
        self.startRecordBtn.setText(_translate("MainWindow", "Start Recording"))
        self.stopRecordBtn.setText(_translate("MainWindow", "Stop Recording"))
        self.moveFile.setText(_translate("MainWindow", "Move File"))
        self.deleteFile.setText(_translate("MainWindow", "Delete File"))
        self.actionBoard_Setting.setText(_translate("MainWindow", "Board Setting"))
        self.action_info.setText(_translate("MainWindow", "New"))
        self.action_About_us.setText(_translate("MainWindow", "&About us"))
        self.actionAuto_Congifuration_Wizard.setText(_translate("MainWindow", "Auto-Congifuration Wizard"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionDuplicate.setText(_translate("MainWindow", "Duplicate"))
        self.actionRename.setText(_translate("MainWindow", "Rename"))
        self.actionRemove.setText(_translate("MainWindow", "Remove"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionProfile1.setText(_translate("MainWindow", "Profile1"))
        self.actionSetting.setText(_translate("MainWindow", "Setting"))
from pyqtgraph import PlotWidget