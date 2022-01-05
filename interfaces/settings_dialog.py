from collections import namedtuple

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QMainWindow, QWidget, QPushButton, QGridLayout, QLabel
from NekrodWidgets import ColorSelectButton

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
                set_widget.setObjectName("submenu")
                set_widget.clicked.connect(setting.method)

            new_widget.horizontalLayout.addWidget(set_widget)
            self.SettingsAreaLayout.addWidget(new_widget)

    def setting_color_theme(self):
        new_dialog = QDialog()
        new_dialog.setWindowTitle("Change Color Theme")
        new_dialog.resize(300, 100)

        new_dialog.setParent(self, Qt.Window)
        new_layout = QGridLayout()
        new_dialog.setLayout(new_layout)

        primary_label = QLabel("Основной цвет")
        primary_button = ColorSelectButton()

        secondary_label = QLabel("Дополнительный цвет")
        secondary_button = ColorSelectButton()

        background_label = QLabel("Цвет фона")
        background_button = ColorSelectButton()

        new_layout.addWidget(primary_label, 0, 0)
        new_layout.addWidget(primary_button, 1, 0)

        new_layout.addWidget(secondary_label, 0, 1)
        new_layout.addWidget(secondary_button, 1, 1)

        new_layout.addWidget(background_label, 0, 2)
        new_layout.addWidget(background_button, 1, 2)

        new_dialog.exec()
