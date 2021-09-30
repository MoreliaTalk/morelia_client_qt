import sys
from os import path

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui

from interfaces.main_window import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.CustomTitleBar.installEventFilter(self)

        self.theme = "dark"

        if self.theme == "dark":
            self.setStyleSheet(open(
                path.join("styles", "dark_theme.css"), "r"
            ).read())

    def eventFilter(self, object: QtCore.QObject, event: QtCore.QEvent):
        if object == self.CustomTitleBar:
            if isinstance(event, QtGui.QMouseEvent):
                if event.type() == QtCore.QEvent.Type.MouseButtonPress and event.button() == QtCore.Qt.LeftButton:
                    self.windowHandle().startSystemMove()

        return super().eventFilter(object, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
