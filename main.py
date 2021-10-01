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

        self.window_resize_border = 3
        self.installEventFilter(self)
        self.CustomTitleBar.installEventFilter(self)

        self.theme = "dark"

        if self.theme == "dark":
            self.setStyleSheet(open(
                path.join("styles", "dark_theme.css"), "r"
            ).read())

    def eventFilter(self, object: QtCore.QObject, event: QtCore.QEvent):
        if object == self.CustomTitleBar:
            if isinstance(event, QtGui.QMouseEvent):
                if (event.type() == QtCore.QEvent.Type.MouseButtonPress and
                        event.button() == QtCore.Qt.LeftButton and
                        event.pos().y() > (self.window_resize_border) and
                        event.pos().y() < (self.CustomTitleBar.height())):
                    self.windowHandle().startSystemMove()
        elif object == self:
            if isinstance(event, QtGui.QMouseEvent):
                if (event.type() == QtCore.QEvent.Type.MouseButtonPress and
                        event.button() == QtCore.Qt.LeftButton):
                    if event.pos().x() <= self.window_resize_border:
                        self.windowHandle().startSystemResize(QtCore.Qt.Edge.LeftEdge)
                    elif (event.pos().x() - self.width()) >= -self.window_resize_border:
                        self.windowHandle().startSystemResize(QtCore.Qt.Edge.RightEdge)
                    elif event.pos().y() <= self.window_resize_border:
                        self.windowHandle().startSystemResize(QtCore.Qt.Edge.TopEdge)
                    elif (event.pos().y() - self.height()) >= -self.window_resize_border:
                        self.windowHandle().startSystemResize(QtCore.Qt.Edge.BottomEdge)

            elif isinstance(event, QtGui.QHoverEvent):
                if (event.pos().x() <= self.window_resize_border or
                        (event.pos().x() - self.width()) >= -self.window_resize_border):
                    self.setCursor(QtCore.Qt.CursorShape.SizeHorCursor)
                elif (event.pos().y() <= self.window_resize_border or
                        (event.pos().y() - self.height()) >= -self.window_resize_border):
                    self.setCursor(QtCore.Qt.CursorShape.SizeVerCursor)
                else:
                    self.setCursor(QtCore.Qt.CursorShape.ArrowCursor)

        return super().eventFilter(object, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
