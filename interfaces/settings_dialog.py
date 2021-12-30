import sys
from collections import namedtuple

from PySide6.QtCore import Qt, QMetaObject, QCoreApplication
from PySide6.QtWidgets import QDialog, QMainWindow, QWidget, QPushButton

from interfaces.raw.setting_card import Ui_SettingCard
from interfaces.raw.settings_dialog import Ui_SettingsDialog


class SettingItem(Ui_SettingCard, QWidget):
    def __init__(self):
        super(SettingItem, self).__init__()

        self.setupUi(self)


class SettingsDialog(Ui_SettingsDialog, QDialog):
    def __init__(self, parent: QMainWindow):
        super(SettingsDialog, self).__init__()

        self.setupUi(self)
        self.setParent(parent, Qt.Window)
        self.setWindowTitle("Settings")

        SettingListItem = namedtuple("SettingsListItem", "name type method")
        self.SETTINGS_LIST = [
            SettingListItem(
                name="Тема оформления",
                type="button",
                method=self.setting_color_theme
            )
        ]

        self.load_settings()

    def load_settings(self):
        for setting in self.SETTINGS_LIST:
            new_widget = SettingItem()
            new_widget.label.setText(f"<b>{setting.name}</b>")

            if setting.type == "button":
                set_widget = QPushButton("Редактировать")
                set_widget.clicked.connect(setting.method)

            new_widget.horizontalLayout.addWidget(set_widget)
            self.SettingsAreaLayout.addWidget(new_widget)

    def setting_color_theme(self):
        a = QDialog()

        a.exec()