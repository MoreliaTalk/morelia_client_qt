import sys

from PySide6.QtWidgets import QDialog, QApplication

from interfaces.raw.settings_dialog import Ui_SettingsDialog


class SettingsDialog(Ui_SettingsDialog, QDialog):
    def __init__(self):
        super(SettingsDialog, self).__init__()
