import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QMainWindow

from interfaces.raw.settings_dialog import Ui_SettingsDialog


class SettingsDialog(Ui_SettingsDialog, QDialog):
    def __init__(self, parent: QMainWindow):
        super(SettingsDialog, self).__init__()
        self.setParent(parent, Qt.Window)
