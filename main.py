from PyQt5 import QtWidgets, QtCore, QtGui
from module.main_window import Ui_MainWindow

class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

        self.theme = "dark"
        if self.theme:
            if self.theme == "dark":
                css = open('styles/black.css', 'r')
                self.styleData = css.read()
                css.close()
                self.ExitButton.setIcon(QtGui.QIcon("svg/exit_white.svg"))
                self.MinimazeButton.setIcon(QtGui.QIcon("svg/mini_white.svg"))


        self.setStyleSheet(self.styleData)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.MinimazeButton.setIconSize(QtCore.QSize(13, 13))
        self.ExitButton.setIconSize(QtCore.QSize(10, 10))
        
        self.ExitButton.clicked.connect(self.close)
        self.MinimazeButton.clicked.connect(self.showMinimized)
        self.ResizeButton.clicked.connect(self.resize_window)

    def resize_window(self):
        self.showMaximized()

    def theme_change(self):
        pass

app = QtWidgets.QApplication([])
window = Main()
window.show()
app.exec_()