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

    def eventFilter(self, obj: QtCore.QObject, event: QtCore.QEvent):
        if obj == self.CustomTitleBar:
            if isinstance(event, QtGui.QMouseEvent):
                if (event.type() == QtCore.QEvent.Type.MouseButtonPress and
                        event.button() == QtCore.Qt.LeftButton and
                        event.pos().y() > (self.window_resize_border) and
                        event.pos().y() < (self.CustomTitleBar.height())):
                    self.windowHandle().startSystemMove()
        elif obj == self:
            if isinstance(event, QtGui.QMouseEvent):
                if (event.type() == QtCore.QEvent.Type.MouseButtonPress and
                        event.button() == QtCore.Qt.LeftButton):
                    edges = QtCore.Qt.Edges()

                    if event.pos().x() <= self.window_resize_border:
                        edges |= QtCore.Qt.Edge.LeftEdge
                    if (event.pos().x() - self.width()) >= -self.window_resize_border:
                        edges |= QtCore.Qt.Edge.RightEdge
                    if event.pos().y() <= self.window_resize_border:
                        edges |= QtCore.Qt.Edge.TopEdge
                    if (event.pos().y() - self.height()) >= -self.window_resize_border:
                        edges |= QtCore.Qt.Edge.BottomEdge

                    if edges:
                        self.windowHandle().startSystemResize(edges)

            elif isinstance(event, QtGui.QHoverEvent):
                if ((event.pos().x() <= self.window_resize_border and
                        event.pos().y() <= self.window_resize_border) or
                        ((event.pos().x() - self.width()) >= -self.window_resize_border and
                            (event.pos().y() - self.height()) >= -self.window_resize_border)):
                    self.setCursor(QtCore.Qt.CursorShape.SizeFDiagCursor)
                elif ((event.pos().x() <= self.window_resize_border and
                        (event.pos().y() - self.height()) >= -self.window_resize_border) or
                        ((event.pos().x() - self.width()) >= -self.window_resize_border and
                            event.pos().y() <= self.window_resize_border)):
                    self.setCursor(QtCore.Qt.CursorShape.SizeBDiagCursor)
                elif (event.pos().x() <= self.window_resize_border or
                        (event.pos().x() - self.width()) >= -self.window_resize_border):
                    self.setCursor(QtCore.Qt.CursorShape.SizeHorCursor)
                elif (event.pos().y() <= self.window_resize_border or
                        (event.pos().y() - self.height()) >= -self.window_resize_border):
                    self.setCursor(QtCore.Qt.CursorShape.SizeVerCursor)
                else:
                    self.setCursor(QtCore.Qt.CursorShape.ArrowCursor)

        return super().eventFilter(obj, event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
