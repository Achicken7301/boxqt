from PyQt5 import QtWidgets, QtGui
from ui.profile_options import Ui_ProfileSettings
from utils.punching_bag import *


class User:

    def __init__(self,
                 meas_sys: bool = True,
                 name: str = "name",
                 age: int = 0,
                 height: float = 0.0,
                 weight: float = 0.0) -> None:
        self.metric_sys = meas_sys
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class ProfileOptionsDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ProfileSettings()
        self.ui.setupUi(self)

        # import modules
        self.bag = PunchingBag()
        self.user = User()
        
        # Load from DATABASE

        # bag style initial setup
        self.hanging_radioBtn_checked()

        # measurement system style initial setup
        self.metric_system_radioBtn_checked()

        # radio button initial setup
        self.ui.hanging_bag_radio_button.setChecked(True)
        self.ui.metric_system_radioBtn.setChecked(True)

        # RadioBtn punching bag condition
        self.ui.freestanding_bag_radio_button.clicked.connect(
            self.freestanding_radioBtn_checked)
        self.ui.hanging_bag_radio_button.clicked.connect(
            self.hanging_radioBtn_checked)

        # RadioBtn measurement system condition
        self.ui.metric_system_radioBtn.clicked.connect(
            self.metric_system_radioBtn_checked)
        self.ui.imperial_system_radioBtn.clicked.connect(
            self.imperial_system_radioBtn_checked)

        # Accept
        self.ui.buttonBox.accepted.connect(self.accepted)

    def accepted(self):
        # Punching bag settings
        if self.ui.hanging_bag_radio_button.isChecked():
            self.bag.hanging_style = True
        elif self.ui.freestanding_bag_radio_button.isChecked():
            self.bag.hanging_style = False

        self.bag.length = float(self.ui.punching_bag_input_length.text())
        self.bag.l2top = float(self.ui.punching_bag_input_height2top.text())
        self.bag.l2btm = float(self.ui.punching_bag_input_btm2gnd.text())
        self.bag.mass = float(self.ui.punching_bag_input_weight.text())

        # User settings
        if self.ui.metric_system_radioBtn.isChecked():
            self.user.metric_sys = True
        elif self.ui.imperial_system_radioBtn.isChecked():
            self.user.metric_sys = False

        self.user.name = self.ui.user_input_name.text()
        self.user.age = int(self.ui.user_input_age.text())
        self.user.height = float(self.ui.user_input_height.text())
        self.user.weight = self.ui.user_input_weight.text()
        
        # TODO: FURTURE Store to Database
        

    def imperial_system_radioBtn_checked(self):
        # user
        self.ui.user_height_dimension.setText("ft")
        self.ui.user_weight_dimension.setText("lbs")
        
        # punching bah
        self.ui.punching_bag_bottom2ground_dimension.setText("ft")
        self.ui.punching_bag_height2top_dimension.setText("ft")
        self.ui.punching_bag_length_dimension.setText("ft")
        self.ui.punching_bag_weight_dimension.setText("lbs")

    def metric_system_radioBtn_checked(self):
        # user
        self.ui.user_height_dimension.setText("cm")
        self.ui.user_weight_dimension.setText("kg")
        
        # punching bag
        self.ui.punching_bag_bottom2ground_dimension.setText("cm")
        self.ui.punching_bag_height2top_dimension.setText("cm")
        self.ui.punching_bag_length_dimension.setText("cm")
        self.ui.punching_bag_weight_dimension.setText("kg")

    def freestanding_radioBtn_checked(self):
        self.ui.punching_bag_style.setPixmap(
            QtGui.QPixmap("boxing-gui/images/freestanding.png"))
        self.ui.punching_bag_style_name.setText(
            "### Freestanding Punching Bag")

    def hanging_radioBtn_checked(self):
        self.ui.punching_bag_style.setPixmap(
            QtGui.QPixmap("boxing-gui/images/hanging.png"))
        self.ui.punching_bag_style_name.setText("### Hanging Punching Bag")
