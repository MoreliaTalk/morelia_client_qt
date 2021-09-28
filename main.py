import sys
from os import path

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore

from interfaces.main_window import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        # self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

        self.theme = "dark"

        if self.theme == "dark":
            self.setStyleSheet(open(
                path.join("styles", "dark_theme.css"), "r"
            ).read())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
