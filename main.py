from PyQt5 import QtWidgets, QtCore, QtGui
from module.main_window import Ui_MainWindow
from module import message

QtCore.QCoreApplication.addLibraryPath("./plugins");

class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.moving = False
        QtGui.QFontDatabase.addApplicationFont("font/Ustroke.ttf")
        QtGui.QFontDatabase.addApplicationFont("font/Natural Mono Regular.ttf")

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
        self.MinimazeButton.pressed.connect(self.ButtonPressedMovingFalse)
        self.ExitButton.pressed.connect(self.ButtonPressedMovingFalse)

        self.SCROLmessage = self.MessagePole.verticalScrollBar()

        self.MessagesControler = message.MessageGrid()
        self.scrollAreaWidgetContents.setLayout(self.MessagesControler)
        self.SendButton.setIcon(QtGui.QIcon("svg/sendg.svg"))
        self.SendButton.setIconSize(QtCore.QSize(40, 40))

        self.SCROLmessage.rangeChanged.connect(lambda x, y: self.SCROLmessage.setValue(y))
        self.SendButton.clicked.connect(self.sendMes)

    def ButtonPressedMovingFalse(self):
        self.moving = False

    def mousePressEvent(self, event):
        if event.y() <= 30:
            if event.button() == QtCore.Qt.LeftButton:
                self.moving = True
                self.offset = event.pos()
        else:
            self.moving = False

    def mouseMoveEvent(self, event):
        if self.moving:
            self.move(event.globalPos()-self.offset)

    def theme_change(self):
        pass

    def sendMes(self):
        self.MessagePole.hide()
        self.MessagesControler.addOtherMessage(self.InputText.toPlainText(), "10:00")
        self.MessagesControler.addMyMessage(self.InputText.toPlainText(), "10:00")
        self.MessagePole.show()


app = QtWidgets.QApplication([])
window = Main()
window.show()
app.exec_()
