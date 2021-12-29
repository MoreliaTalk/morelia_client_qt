import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QMainWindow, QWidget, QHBoxLayout, QLabel

from interfaces.raw.setting_card import Ui_SettingCard
from interfaces.raw.settings_dialog import Ui_SettingsDialog


class SettingItem(Ui_SettingCard, QWidget):
    def __init__(self):
        super(SettingItem, self).__init__()

        self.setupUi(self)


class SettingsDialog(Ui_SettingsDialog, QDialog):
    class SettingListItem:
        def __init__(self,
                     name: str,
                     type_setting: str,
                     method: object):
            self.name = name
            self.type = type_setting
            self.method = method

    SETTINGS_LIST = [
        SettingListItem(
            "Тема оформления",
            "button",
            "none"
        )
    ]

    def __init__(self, parent: QMainWindow):
        super(SettingsDialog, self).__init__()

        self.setupUi(self)
        self.setParent(parent, Qt.Window)
        self.setWindowTitle("Settings")

        self.load_settings()

    def load_settings(self):
        for setting in self.SETTINGS_LIST:
            new_widget = SettingItem()
            new_widget.label.setText(setting.name)

            self.SettingsAreaLayout.addWidget(new_widget)