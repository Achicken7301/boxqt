# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\laragon\www\boxqt\boxing-gui\ui\history.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HistoryDialog(object):
    def setupUi(self, HistoryDialog):
        HistoryDialog.setObjectName("HistoryDialog")
        HistoryDialog.resize(709, 478)
        self.gridLayout = QtWidgets.QGridLayout(HistoryDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeView = QtWidgets.QTreeView(HistoryDialog)
        self.treeView.setObjectName("treeView")
        self.horizontalLayout.addWidget(self.treeView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(HistoryDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.acel_chart = PlotWidget(HistoryDialog)
        self.acel_chart.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acel_chart.sizePolicy().hasHeightForWidth())
        self.acel_chart.setSizePolicy(sizePolicy)
        self.acel_chart.setAutoFillBackground(True)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.acel_chart.setProperty("backgroundBrush", brush)
        self.acel_chart.setObjectName("acel_chart")
        self.verticalLayout.addWidget(self.acel_chart)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(HistoryDialog)
        QtCore.QMetaObject.connectSlotsByName(HistoryDialog)

    def retranslateUi(self, HistoryDialog):
        _translate = QtCore.QCoreApplication.translate
        HistoryDialog.setWindowTitle(_translate("HistoryDialog", "History Punches"))
        self.label.setText(_translate("HistoryDialog", "acceleration"))
from pyqtgraph import PlotWidget
