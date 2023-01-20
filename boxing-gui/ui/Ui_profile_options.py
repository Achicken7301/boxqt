# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\laragon\www\boxqt\boxing-gui\ui\profile_options.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProfileSettings(object):
    def setupUi(self, ProfileSettings):
        ProfileSettings.setObjectName("ProfileSettings")
        ProfileSettings.resize(651, 550)
        self.gridLayout_4 = QtWidgets.QGridLayout(ProfileSettings)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.line_2 = QtWidgets.QFrame(ProfileSettings)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 0, 1, 5, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(ProfileSettings)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(ProfileSettings)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(ProfileSettings)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.punching_bag_input_height2top = QtWidgets.QLineEdit(ProfileSettings)
        self.punching_bag_input_height2top.setObjectName("punching_bag_input_height2top")
        self.gridLayout_2.addWidget(self.punching_bag_input_height2top, 6, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(ProfileSettings)
        self.label_4.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.punching_bag_bottom2ground_dimension = QtWidgets.QLabel(ProfileSettings)
        self.punching_bag_bottom2ground_dimension.setObjectName("punching_bag_bottom2ground_dimension")
        self.gridLayout_2.addWidget(self.punching_bag_bottom2ground_dimension, 8, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(ProfileSettings)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 2, 0, 1, 1)
        self.punching_bag_input_weight = QtWidgets.QLineEdit(ProfileSettings)
        self.punching_bag_input_weight.setObjectName("punching_bag_input_weight")
        self.gridLayout_2.addWidget(self.punching_bag_input_weight, 4, 1, 1, 1)
        self.punching_bag_weight_dimension = QtWidgets.QLabel(ProfileSettings)
        self.punching_bag_weight_dimension.setObjectName("punching_bag_weight_dimension")
        self.gridLayout_2.addWidget(self.punching_bag_weight_dimension, 4, 2, 1, 1)
        self.punching_bag_input_btm2gnd = QtWidgets.QLineEdit(ProfileSettings)
        self.punching_bag_input_btm2gnd.setObjectName("punching_bag_input_btm2gnd")
        self.gridLayout_2.addWidget(self.punching_bag_input_btm2gnd, 8, 1, 1, 1)
        self.freestanding_bag_radio_button = QtWidgets.QRadioButton(ProfileSettings)
        self.freestanding_bag_radio_button.setObjectName("freestanding_bag_radio_button")
        self.punching_bag_style_button = QtWidgets.QButtonGroup(ProfileSettings)
        self.punching_bag_style_button.setObjectName("punching_bag_style_button")
        self.punching_bag_style_button.addButton(self.freestanding_bag_radio_button)
        self.gridLayout_2.addWidget(self.freestanding_bag_radio_button, 3, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(ProfileSettings)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 8, 0, 1, 1)
        self.punching_bag_length_dimension = QtWidgets.QLabel(ProfileSettings)
        self.punching_bag_length_dimension.setObjectName("punching_bag_length_dimension")
        self.gridLayout_2.addWidget(self.punching_bag_length_dimension, 5, 2, 1, 1)
        self.hanging_bag_radio_button = QtWidgets.QRadioButton(ProfileSettings)
        self.hanging_bag_radio_button.setChecked(True)
        self.hanging_bag_radio_button.setObjectName("hanging_bag_radio_button")
        self.punching_bag_style_button.addButton(self.hanging_bag_radio_button)
        self.gridLayout_2.addWidget(self.hanging_bag_radio_button, 2, 1, 1, 1)
        self.punching_bag_input_length = QtWidgets.QLineEdit(ProfileSettings)
        self.punching_bag_input_length.setObjectName("punching_bag_input_length")
        self.gridLayout_2.addWidget(self.punching_bag_input_length, 5, 1, 1, 1)
        self.punching_bag_height2top_dimension = QtWidgets.QLabel(ProfileSettings)
        self.punching_bag_height2top_dimension.setObjectName("punching_bag_height2top_dimension")
        self.gridLayout_2.addWidget(self.punching_bag_height2top_dimension, 6, 2, 1, 1)
        self.line = QtWidgets.QFrame(ProfileSettings)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 3, 2, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 4, 3, 1, 1)
        self.punching_bag_style_name = QtWidgets.QLabel(ProfileSettings)
        self.punching_bag_style_name.setFrameShadow(QtWidgets.QFrame.Plain)
        self.punching_bag_style_name.setLineWidth(1)
        self.punching_bag_style_name.setTextFormat(QtCore.Qt.MarkdownText)
        self.punching_bag_style_name.setAlignment(QtCore.Qt.AlignCenter)
        self.punching_bag_style_name.setObjectName("punching_bag_style_name")
        self.gridLayout_4.addWidget(self.punching_bag_style_name, 5, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(ProfileSettings)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_4.addWidget(self.line_3, 5, 2, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(ProfileSettings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_4.addWidget(self.buttonBox, 6, 2, 1, 1)
        self.punching_bag_style = QtWidgets.QLabel(ProfileSettings)
        self.punching_bag_style.setObjectName("punching_bag_style")
        self.gridLayout_4.addWidget(self.punching_bag_style, 1, 0, 4, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        self.user_input_age = QtWidgets.QLineEdit(ProfileSettings)
        self.user_input_age.setObjectName("user_input_age")
        self.gridLayout.addWidget(self.user_input_age, 3, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(ProfileSettings)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 5, 0, 1, 1)
        self.user_weight_dimension = QtWidgets.QLabel(ProfileSettings)
        self.user_weight_dimension.setObjectName("user_weight_dimension")
        self.gridLayout.addWidget(self.user_weight_dimension, 5, 2, 1, 1)
        self.user_input_weight = QtWidgets.QLineEdit(ProfileSettings)
        self.user_input_weight.setObjectName("user_input_weight")
        self.gridLayout.addWidget(self.user_input_weight, 5, 1, 1, 1)
        self.user_input_name = QtWidgets.QLineEdit(ProfileSettings)
        self.user_input_name.setObjectName("user_input_name")
        self.gridLayout.addWidget(self.user_input_name, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(ProfileSettings)
        self.label_2.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(ProfileSettings)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 3, 0, 1, 1)
        self.user_input_height = QtWidgets.QLineEdit(ProfileSettings)
        self.user_input_height.setObjectName("user_input_height")
        self.gridLayout.addWidget(self.user_input_height, 4, 1, 1, 1)
        self.user_height_dimension = QtWidgets.QLabel(ProfileSettings)
        self.user_height_dimension.setObjectName("user_height_dimension")
        self.gridLayout.addWidget(self.user_height_dimension, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(ProfileSettings)
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(ProfileSettings)
        self.label_3.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(ProfileSettings)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 0, 0, 1, 3)
        self.gridLayout_4.addLayout(self.gridLayout, 2, 2, 1, 2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comboBox_2 = QtWidgets.QComboBox(ProfileSettings)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_3.addWidget(self.comboBox_2, 2, 1, 2, 1)
        self.label_19 = QtWidgets.QLabel(ProfileSettings)
        self.label_19.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(ProfileSettings)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_3.addWidget(self.comboBox, 1, 1, 1, 1)
        self.imperial_system_radioBtn = QtWidgets.QRadioButton(ProfileSettings)
        self.imperial_system_radioBtn.setObjectName("imperial_system_radioBtn")
        self.measurement_system = QtWidgets.QButtonGroup(ProfileSettings)
        self.measurement_system.setObjectName("measurement_system")
        self.measurement_system.addButton(self.imperial_system_radioBtn)
        self.gridLayout_3.addWidget(self.imperial_system_radioBtn, 3, 0, 1, 1)
        self.metric_system_radioBtn = QtWidgets.QRadioButton(ProfileSettings)
        self.metric_system_radioBtn.setChecked(True)
        self.metric_system_radioBtn.setObjectName("metric_system_radioBtn")
        self.measurement_system.addButton(self.metric_system_radioBtn)
        self.gridLayout_3.addWidget(self.metric_system_radioBtn, 1, 0, 2, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 1, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 2, 1, 2)

        self.retranslateUi(ProfileSettings)
        self.buttonBox.rejected.connect(ProfileSettings.reject) # type: ignore
        self.buttonBox.accepted.connect(ProfileSettings.accept) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ProfileSettings)
        ProfileSettings.setTabOrder(self.metric_system_radioBtn, self.imperial_system_radioBtn)
        ProfileSettings.setTabOrder(self.imperial_system_radioBtn, self.user_input_name)
        ProfileSettings.setTabOrder(self.user_input_name, self.user_input_age)
        ProfileSettings.setTabOrder(self.user_input_age, self.user_input_height)
        ProfileSettings.setTabOrder(self.user_input_height, self.user_input_weight)
        ProfileSettings.setTabOrder(self.user_input_weight, self.hanging_bag_radio_button)
        ProfileSettings.setTabOrder(self.hanging_bag_radio_button, self.freestanding_bag_radio_button)
        ProfileSettings.setTabOrder(self.freestanding_bag_radio_button, self.punching_bag_input_weight)
        ProfileSettings.setTabOrder(self.punching_bag_input_weight, self.punching_bag_input_length)
        ProfileSettings.setTabOrder(self.punching_bag_input_length, self.punching_bag_input_height2top)
        ProfileSettings.setTabOrder(self.punching_bag_input_height2top, self.punching_bag_input_btm2gnd)
        ProfileSettings.setTabOrder(self.punching_bag_input_btm2gnd, self.comboBox)
        ProfileSettings.setTabOrder(self.comboBox, self.comboBox_2)

    def retranslateUi(self, ProfileSettings):
        _translate = QtCore.QCoreApplication.translate
        ProfileSettings.setWindowTitle(_translate("ProfileSettings", "Profile Settings"))
        self.label_7.setText(_translate("ProfileSettings", "Height from top to ... (d):"))
        self.label_6.setText(_translate("ProfileSettings", "Length (L): "))
        self.label_5.setText(_translate("ProfileSettings", "Weight:"))
        self.punching_bag_input_height2top.setText(_translate("ProfileSettings", "0.0"))
        self.label_4.setText(_translate("ProfileSettings", "**Punching Bag Infomation**"))
        self.punching_bag_bottom2ground_dimension.setText(_translate("ProfileSettings", "cm"))
        self.label_13.setText(_translate("ProfileSettings", "Punching bag Style"))
        self.punching_bag_input_weight.setText(_translate("ProfileSettings", "0.0"))
        self.punching_bag_weight_dimension.setText(_translate("ProfileSettings", "kg"))
        self.punching_bag_input_btm2gnd.setText(_translate("ProfileSettings", "0.0"))
        self.freestanding_bag_radio_button.setText(_translate("ProfileSettings", "Freestanding Punching Bag"))
        self.label_8.setText(_translate("ProfileSettings", "Height from bottm to ... (g):"))
        self.punching_bag_length_dimension.setText(_translate("ProfileSettings", "cm"))
        self.hanging_bag_radio_button.setText(_translate("ProfileSettings", "Hanging Punching Bag"))
        self.punching_bag_input_length.setText(_translate("ProfileSettings", "0.0"))
        self.punching_bag_height2top_dimension.setText(_translate("ProfileSettings", "cm"))
        self.punching_bag_style_name.setText(_translate("ProfileSettings", "### Hanging Punching Bag"))
        self.punching_bag_style.setText(_translate("ProfileSettings", "TextLabel"))
        self.user_input_age.setText(_translate("ProfileSettings", "0"))
        self.label_15.setText(_translate("ProfileSettings", "Weight"))
        self.user_weight_dimension.setText(_translate("ProfileSettings", "kg"))
        self.user_input_weight.setText(_translate("ProfileSettings", "0.0"))
        self.user_input_name.setText(_translate("ProfileSettings", "fullname"))
        self.label_2.setText(_translate("ProfileSettings", "Full name:"))
        self.label_17.setText(_translate("ProfileSettings", "Age"))
        self.user_input_height.setText(_translate("ProfileSettings", "0.0"))
        self.user_height_dimension.setText(_translate("ProfileSettings", "cm"))
        self.label.setText(_translate("ProfileSettings", "**User Infomation**"))
        self.label_3.setText(_translate("ProfileSettings", "Height:"))
        self.label_19.setText(_translate("ProfileSettings", "**Measurement System**"))
        self.imperial_system_radioBtn.setText(_translate("ProfileSettings", "‎Imperial system"))
        self.metric_system_radioBtn.setText(_translate("ProfileSettings", "Metric system"))