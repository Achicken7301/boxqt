# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\laragon\www\boxqt\boxing-gui\ui\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(943, 542)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.chart_display_layout = QtWidgets.QVBoxLayout()
        self.chart_display_layout.setContentsMargins(10, -1, 10, -1)
        self.chart_display_layout.setObjectName("chart_display_layout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.chart_display_layout.addWidget(self.label_3)
        self.acceleration_chart = PlotWidget(self.centralwidget)
        self.acceleration_chart.setEnabled(False)
        self.acceleration_chart.setAutoFillBackground(True)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.acceleration_chart.setProperty("backgroundBrush", brush)
        self.acceleration_chart.setObjectName("acceleration_chart")
        self.chart_display_layout.addWidget(self.acceleration_chart)
        self.gridLayout.addLayout(self.chart_display_layout, 5, 2, 2, 2)
        self.number_display_layout = QtWidgets.QVBoxLayout()
        self.number_display_layout.setContentsMargins(10, 0, 10, 0)
        self.number_display_layout.setObjectName("number_display_layout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 6, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 0, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 4, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_14.setFont(font)
        self.label_14.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 5, 0, 1, 1)
        self.current_force_line = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_force_line.sizePolicy().hasHeightForWidth())
        self.current_force_line.setSizePolicy(sizePolicy)
        self.current_force_line.setMaximumSize(QtCore.QSize(300, 16777215))
        self.current_force_line.setReadOnly(True)
        self.current_force_line.setObjectName("current_force_line")
        self.gridLayout_3.addWidget(self.current_force_line, 0, 1, 1, 1)
        self.peak_force_line = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.peak_force_line.sizePolicy().hasHeightForWidth())
        self.peak_force_line.setSizePolicy(sizePolicy)
        self.peak_force_line.setMaximumSize(QtCore.QSize(300, 16777215))
        self.peak_force_line.setReadOnly(True)
        self.peak_force_line.setObjectName("peak_force_line")
        self.gridLayout_3.addWidget(self.peak_force_line, 2, 1, 1, 1)
        self.average_force_line = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.average_force_line.sizePolicy().hasHeightForWidth())
        self.average_force_line.setSizePolicy(sizePolicy)
        self.average_force_line.setMaximumSize(QtCore.QSize(300, 16777215))
        self.average_force_line.setReadOnly(True)
        self.average_force_line.setObjectName("average_force_line")
        self.gridLayout_3.addWidget(self.average_force_line, 4, 1, 1, 1)
        self.number_of_punches = QtWidgets.QLineEdit(self.centralwidget)
        self.number_of_punches.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number_of_punches.sizePolicy().hasHeightForWidth())
        self.number_of_punches.setSizePolicy(sizePolicy)
        self.number_of_punches.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.number_of_punches.setFont(font)
        self.number_of_punches.setReadOnly(True)
        self.number_of_punches.setObjectName("number_of_punches")
        self.gridLayout_3.addWidget(self.number_of_punches, 5, 1, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy)
        self.lineEdit_11.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_3.addWidget(self.lineEdit_11, 6, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 2, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 4, 2, 1, 1)
        self.number_display_layout.addLayout(self.gridLayout_3)
        self.gridLayout.addLayout(self.number_display_layout, 5, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 5, 1, 2, 1)
        self.history_layout = QtWidgets.QGridLayout()
        self.history_layout.setObjectName("history_layout")
        self.log_check = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_check.sizePolicy().hasHeightForWidth())
        self.log_check.setSizePolicy(sizePolicy)
        self.log_check.setObjectName("log_check")
        self.history_layout.addWidget(self.log_check, 2, 0, 1, 1)
        self.history_table = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.history_table.sizePolicy().hasHeightForWidth())
        self.history_table.setSizePolicy(sizePolicy)
        self.history_table.setMaximumSize(QtCore.QSize(500, 16777215))
        self.history_table.setObjectName("history_table")
        self.history_layout.addWidget(self.history_table, 1, 0, 1, 1)
        self.save_folder_button = QtWidgets.QToolButton(self.centralwidget)
        self.save_folder_button.setObjectName("save_folder_button")
        self.history_layout.addWidget(self.save_folder_button, 4, 0, 1, 1)
        self.save_folder_line = QtWidgets.QLineEdit(self.centralwidget)
        self.save_folder_line.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_folder_line.sizePolicy().hasHeightForWidth())
        self.save_folder_line.setSizePolicy(sizePolicy)
        self.save_folder_line.setMaximumSize(QtCore.QSize(400, 16777215))
        self.save_folder_line.setAutoFillBackground(False)
        self.save_folder_line.setReadOnly(True)
        self.save_folder_line.setObjectName("save_folder_line")
        self.history_layout.addWidget(self.save_folder_line, 3, 0, 1, 1)
        self.gridLayout.addLayout(self.history_layout, 6, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 4)
        self.toolbar_layout = QtWidgets.QHBoxLayout()
        self.toolbar_layout.setContentsMargins(10, -1, 10, -1)
        self.toolbar_layout.setObjectName("toolbar_layout")
        self.start_button = QtWidgets.QToolButton(self.centralwidget)
        self.start_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\laragon\\www\\boxqt\\boxing-gui\\ui\\icons/start.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.start_button.setIcon(icon)
        self.start_button.setIconSize(QtCore.QSize(24, 24))
        self.start_button.setAutoExclusive(False)
        self.start_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.start_button.setAutoRaise(True)
        self.start_button.setObjectName("start_button")
        self.toolbar_layout.addWidget(self.start_button)
        self.stop_button = QtWidgets.QToolButton(self.centralwidget)
        self.stop_button.setEnabled(False)
        self.stop_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("d:\\laragon\\www\\boxqt\\boxing-gui\\ui\\icons/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.stop_button.setIcon(icon1)
        self.stop_button.setIconSize(QtCore.QSize(24, 24))
        self.stop_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.stop_button.setAutoRaise(True)
        self.stop_button.setObjectName("stop_button")
        self.toolbar_layout.addWidget(self.stop_button)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.toolbar_layout.addWidget(self.line_2)
        self.zero_button = QtWidgets.QToolButton(self.centralwidget)
        self.zero_button.setEnabled(False)
        self.zero_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("d:\\laragon\\www\\boxqt\\boxing-gui\\ui\\icons/zero.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.zero_button.setIcon(icon2)
        self.zero_button.setIconSize(QtCore.QSize(24, 24))
        self.zero_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.zero_button.setAutoRaise(True)
        self.zero_button.setObjectName("zero_button")
        self.toolbar_layout.addWidget(self.zero_button)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.toolbar_layout.addWidget(self.line_3)
        self.option_button = QtWidgets.QToolButton(self.centralwidget)
        self.option_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("d:\\laragon\\www\\boxqt\\boxing-gui\\ui\\icons/option.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.option_button.setIcon(icon3)
        self.option_button.setIconSize(QtCore.QSize(24, 24))
        self.option_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.option_button.setAutoRaise(True)
        self.option_button.setObjectName("option_button")
        self.toolbar_layout.addWidget(self.option_button)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.toolbar_layout.addWidget(self.line_4)
        self.zoom_button = QtWidgets.QToolButton(self.centralwidget)
        self.zoom_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("d:\\laragon\\www\\boxqt\\boxing-gui\\ui\\icons/zoom.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.zoom_button.setIcon(icon4)
        self.zoom_button.setIconSize(QtCore.QSize(24, 24))
        self.zoom_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.zoom_button.setAutoRaise(True)
        self.zoom_button.setObjectName("zoom_button")
        self.toolbar_layout.addWidget(self.zoom_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.toolbar_layout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(48, 48))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setPixmap(QtGui.QPixmap("d:\\laragon\\www\\boxqt\\boxing-gui\\ui\\icons/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.toolbar_layout.addWidget(self.label)
        self.gridLayout.addLayout(self.toolbar_layout, 0, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 943, 26))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuProfile = QtWidgets.QMenu(self.menubar)
        self.menuProfile.setObjectName("menuProfile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_about_this_app = QtWidgets.QAction(MainWindow)
        self.action_about_this_app.setObjectName("action_about_this_app")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.profile_options = QtWidgets.QAction(MainWindow)
        self.profile_options.setObjectName("profile_options")
        self.actionSwitch_Profies = QtWidgets.QAction(MainWindow)
        self.actionSwitch_Profies.setObjectName("actionSwitch_Profies")
        self.menuHelp.addAction(self.action_about_this_app)
        self.menuProfile.addAction(self.actionNew)
        self.menuProfile.addAction(self.profile_options)
        self.menubar.addAction(self.menuProfile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Boxing app"))
        self.label_3.setText(_translate("MainWindow", "Acceleration"))
        self.label_2.setText(_translate("MainWindow", "**Current Force:**"))
        self.label_10.setText(_translate("MainWindow", "**Punches / min:**"))
        self.label_11.setText(_translate("MainWindow", "**Peak Force:**"))
        self.label_12.setText(_translate("MainWindow", "N"))
        self.label_13.setText(_translate("MainWindow", "**Average Force:**"))
        self.label_14.setText(_translate("MainWindow", "**Number of Punches:**"))
        self.label_15.setText(_translate("MainWindow", "N"))
        self.label_16.setText(_translate("MainWindow", "N"))
        self.log_check.setText(_translate("MainWindow", "Log punch history to folder"))
        self.save_folder_button.setText(_translate("MainWindow", "Open history folder"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.zero_button.setText(_translate("MainWindow", "Zero"))
        self.option_button.setText(_translate("MainWindow", "Option"))
        self.zoom_button.setText(_translate("MainWindow", "Zoom"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuProfile.setTitle(_translate("MainWindow", "Profile"))
        self.action_about_this_app.setText(_translate("MainWindow", "About this app"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.profile_options.setText(_translate("MainWindow", "Options"))
        self.actionSwitch_Profies.setText(_translate("MainWindow", "Switch Profie"))
from pyqtgraph import PlotWidget
