from PyQt5 import QtWidgets, QtCore, QtGui
from module.main_window import Ui_MainWindow
import types
from random import random 

class MyMessage(QtWidgets.QGroupBox):
    def __init__(self, textMes):
        super().__init__()
        self.setObjectName("MyMessage")

        timeMes = "13:00"

        textMes = self.textFormat(textMes)

        self.height = 100
        self.width = 100
        
        chetchik = 0
        chetchik_2 = 0

        for i in textMes:
            if i == "\n":
                self.height += 14
                chetchik_2 = chetchik
                chetchik = 0
            else:
                chetchik += 1
                if chetchik >= chetchik_2:
                    self.width += 6


        #print(self.width)

            
        self.setFixedSize(self.width, self.height)
        self.MyMessageText = QtWidgets.QLabel(self)
        self.MyMessageText.setText(textMes)
        self.MyMessageText.setObjectName("MyMessageText")
        self.MyMessageText.move(40, 40)
        font = QtGui.QFont()
        font.setFamily("Natural Mono Regular")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.MyMessageText.setFont(font)

        self.MyMessageTime = QtWidgets.QLabel(self)
        self.MyMessageTime.setText(timeMes)
        self.MyMessageTime.setObjectName("MyMessageTime")
        self.MyMessageTime.move(self.width-50, self.height-40)

    def textFormat(self, text):
        chetchik_line = 0
        returnText = ""
        for i in text:
            chetchik_line += 1

            if chetchik_line == 20:
                returnText += "\n"
                chetchik_line = 0
            else:
                returnText += i

            if i == "\n":
                chetchik_line = 0

        return returnText


class MessageGrid(QtWidgets.QVBoxLayout):
    class MesContainer(QtWidgets.QHBoxLayout):
        def __init__(self, text):
            super().__init__()
            self.addWidget(QtWidgets.QLabel())
            self.addWidget(MyMessage(text))


    def __init__(self, scrollBar):
        super().__init__()

        self.scrollBar = scrollBar

        for i in range(3):
            self.addWidget(QtWidgets.QLabel())

    def addMyMessage(self, text):
        Vbox = QtWidgets.QWidget()
        Vbox.setLayout(self.MesContainer(text))
        self.addWidget(Vbox)

    def addOtherMessage(self, text):
        Vbox = QtWidgets.QWidget()
        Vbox.setLayout(self.MesContainer(text))
        self.addWidget(Vbox)


class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.moving = False
        QtGui.QFontDatabase.addApplicationFont("font/Ustroke.ttf");
        QtGui.QFontDatabase.addApplicationFont("font/Natural Mono Regular.ttf");

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

        self.SCROLmessage = QtWidgets.QScrollBar()
        self.MessagePole.setVerticalScrollBar(self.SCROLmessage)
        self.MessagesControler = MessageGrid(self.SCROLmessage)
        self.scrollAreaWidgetContents.setLayout(self.MessagesControler)

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
        self.MessagesControler.addMyMessage(self.InputText.toPlainText())

app = QtWidgets.QApplication([])
window = Main()
window.show()
app.exec_()