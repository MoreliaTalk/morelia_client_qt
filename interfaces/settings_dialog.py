from collections import namedtuple

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QMainWindow, QWidget, QPushButton, QGridLayout, QLabel, QDialogButtonBox
from NekrodWidgets import ColorSelectButton

from interfaces.raw.setting_card import Ui_SettingCard
from interfaces.raw.settings_dialog import Ui_SettingsDialog
from modules.database.clientdb import ClientDb


class SettingItem(Ui_SettingCard, QWidget):
    def __init__(self):
        super(SettingItem, self).__init__()

        self.setupUi(self)


class SettingsDialog(Ui_SettingsDialog, QDialog):
    def __init__(self, parent: QMainWindow, db: ClientDb):
        super(SettingsDialog, self).__init__()

        self.setupUi(self)
        self.setParent(parent, Qt.Window)
        self.setWindowTitle("Settings")

        self.db = db
        self.main_window = parent

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
        def save_colors():
            self.db.set_param("primary_color", primary_button.color.name())
            self.db.set_param("secondary_color", secondary_button.color.name())
            self.db.set_param("background_color", background_button.color.name())
            self.main_window.set_color_theme()

        new_dialog = QDialog()
        new_dialog.setWindowTitle("Change Color Theme")
        new_dialog.resize(300, 130)

        new_dialog.setParent(self, Qt.Window)
        new_layout = QGridLayout()
        new_dialog.setLayout(new_layout)

        primary_label = QLabel("Основной цвет")
        primary_button = ColorSelectButton(self.db.get_param("primary_color"))

        secondary_label = QLabel("Дополнительный цвет")
        secondary_button = ColorSelectButton(self.db.get_param("secondary_color"))

        background_label = QLabel("Цвет фона")
        background_button = ColorSelectButton(self.db.get_param("background_color"))

        new_layout.addWidget(primary_label, 0, 0)
        new_layout.addWidget(primary_button, 1, 0)

        new_layout.addWidget(secondary_label, 0, 1)
        new_layout.addWidget(secondary_button, 1, 1)

        new_layout.addWidget(background_label, 0, 2)
        new_layout.addWidget(background_button, 1, 2)

        button_box = QDialogButtonBox()
        button_box.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

        for button in button_box.buttons():
            button.setIcon(QIcon())

        button_box.accepted.connect(save_colors)

        new_layout.addWidget(button_box, 2, 0, 1, 3)


        new_dialog.exec()