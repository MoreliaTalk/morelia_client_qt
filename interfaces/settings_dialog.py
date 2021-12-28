import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QMainWindow, QWidget, QHBoxLayout, QLabel

from interfaces.raw.setting_card import Ui_SettingCard
from interfaces.raw.settings_dialog import Ui_SettingsDialog

SETTINGS_LIST = [
    {
        "name": "Тема оформления",
        "type": "combo_box"
    }
]


class SettingItem(Ui_SettingCard, QWidget):
    def __init__(self):
        super(SettingItem, self).__init__()

        self.setupUi(self)


class SettingsDialog(Ui_SettingsDialog, QDialog):
    def __init__(self, parent: QMainWindow):
        super(SettingsDialog, self).__init__()

        self.setupUi(self)
        self.setParent(parent, Qt.Window)

        self.load_settings()

    def load_settings(self):
        for setting in SETTINGS_LIST:

            self.SettingsAreaLayout.addWidget(SettingItem())
