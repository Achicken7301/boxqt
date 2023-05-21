from PyQt5 import QtWidgets, QtGui

# Load UI files
from ui.Ui_profile_options import Ui_ProfileSettings

# import module
from database.User import User
from database.PunchingBag import PunchingBag


class ProfileOptionsDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ProfileSettings()
        self.ui.setupUi(self)

        # bag style & measurement system initial setup
        self.hanging_radioBtn_checked()
        self.metric_system_radioBtn_checked()

        # radio button initial setup
        self.ui.hanging_bag_radio_button.setChecked(True)
        self.ui.metric_system_radioBtn.setChecked(True)

        # RadioBtn punching bag condition
        self.ui.freestanding_bag_radio_button.clicked.connect(
            self.freestanding_radioBtn_checked
        )
        self.ui.hanging_bag_radio_button.clicked.connect(self.hanging_radioBtn_checked)

        # RadioBtn measurement system condition
        self.ui.metric_system_radioBtn.clicked.connect(
            self.metric_system_radioBtn_checked
        )
        self.ui.imperial_system_radioBtn.clicked.connect(
            self.imperial_system_radioBtn_checked
        )

    def save_user_setting(self):
        # User
        user = dict()
        user["name"] = self.ui.user_input_name.text()
        user["age"] = self.ui.user_input_age.text()
        user["height"] = self.ui.user_input_height.text()
        user["weight"] = self.ui.user_input_weight.text()
        user["metric"] = self.if_metric()
        User().save_user_setting(user)

    def save_bag_setting(self):
        # Punching bag
        bag = dict()
        bag["hanging_style"] = self.if_hanging_style()
        bag["length"] = self.ui.punching_bag_input_length.text()
        bag["l2btm"] = self.ui.punching_bag_input_btm2gnd.text()
        bag["l2top"] = self.ui.punching_bag_input_height2top.text()
        bag["weight"] = self.ui.punching_bag_input_weight.text()
        PunchingBag().save_bag_setting(bag)

    def if_metric(self):
        if self.ui.metric_system_radioBtn.isChecked():
            return 1
        elif self.ui.imperial_system_radioBtn.isChecked():
            return 0

    def if_hanging_style(self):
        if self.ui.hanging_bag_radio_button.isChecked():
            return 1
        elif self.ui.freestanding_bag_radio_button.isChecked():
            return 0

    def imperial_system_radioBtn_checked(self):
        self.ui.imperial_system_radioBtn.setChecked(1)

        # user
        self.ui.user_height_dimension.setText("ft")
        self.ui.user_weight_dimension.setText("lbs")

        # punching bah
        self.ui.punching_bag_bottom2ground_dimension.setText("ft")
        self.ui.punching_bag_height2top_dimension.setText("ft")
        self.ui.punching_bag_length_dimension.setText("ft")
        self.ui.punching_bag_weight_dimension.setText("lbs")

    def metric_system_radioBtn_checked(self):
        self.ui.metric_system_radioBtn.setChecked(1)
        # user
        self.ui.user_height_dimension.setText("cm")
        self.ui.user_weight_dimension.setText("kg")

        # punching bag
        self.ui.punching_bag_bottom2ground_dimension.setText("cm")
        self.ui.punching_bag_height2top_dimension.setText("cm")
        self.ui.punching_bag_length_dimension.setText("cm")
        self.ui.punching_bag_weight_dimension.setText("kg")

    def freestanding_radioBtn_checked(self):
        self.ui.freestanding_bag_radio_button.setChecked(True)
        self.ui.punching_bag_style.setPixmap(
            QtGui.QPixmap("boxing-gui/images/freestanding.png")
        )
        self.ui.punching_bag_style_name.setText("### Freestanding Punching Bag")

    def hanging_radioBtn_checked(self):
        self.ui.hanging_bag_radio_button.setChecked(True)
        self.ui.punching_bag_style.setPixmap(
            QtGui.QPixmap("boxing-gui/images/hanging.png")
        )
        self.ui.punching_bag_style_name.setText("### Hanging Punching Bag")
