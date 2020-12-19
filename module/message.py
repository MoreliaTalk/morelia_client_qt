from PyQt5 import QtGui, QtWidgets


class My_and_OU_Message(QtWidgets.QGroupBox):
    def __init__(self, textMes, timeMes, typeMes):
        super().__init__()

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
                    self.width += 10

        self.setFixedSize(self.width, self.height)

        if typeMes == "my":
            self.setObjectName("MyMessage")
            self.MyMessageText = QtWidgets.QLabel(self)
            self.MyMessageText.setText(textMes)
            self.MyMessageText.setObjectName("MessageText")
            self.MyMessageText.move(40, 40)
            font = QtGui.QFont()
            font.setFamily("Natural Mono Regular")
            font.setPointSize(10)
            font.setBold(False)
            font.setWeight(50)
            self.MyMessageText.setFont(font)

            self.MyMessageTime = QtWidgets.QLabel(self)
            self.MyMessageTime.setText(timeMes)
            self.MyMessageTime.setObjectName("MessageTime")
            self.MyMessageTime.move(self.width-50, self.height-40)
        elif typeMes == "OU":
            self.setObjectName("OUMessage")
            self.MyMessageText = QtWidgets.QLabel(self)
            self.MyMessageText.setText(textMes)
            self.MyMessageText.setObjectName("MessageText")
            self.MyMessageText.move(40, 40)
            font = QtGui.QFont()
            font.setFamily("Natural Mono Regular")
            font.setPointSize(10)
            font.setBold(False)
            font.setWeight(50)
            self.MyMessageText.setFont(font)

            self.MyMessageTime = QtWidgets.QLabel(self)
            self.MyMessageTime.setText(timeMes)
            self.MyMessageTime.setObjectName("MessageTime")
            self.MyMessageTime.move(self.width-55, self.height-40)

    def textFormat(self, text):
        chetchik_line = 0
        returnText = ""
        for i in text:
            chetchik_line += 1

            if chetchik_line == 20:
                returnText += "\n"
                returnText += i
                chetchik_line = 1
            else:
                returnText += i

            if i == "\n":
                chetchik_line = 0

        return returnText


class MessageGrid(QtWidgets.QVBoxLayout):
    class MesContainer(QtWidgets.QHBoxLayout):
        def __init__(self, text: str, type_m: str, time):
            super().__init__()
            if type_m == "my":
                self.addWidget(QtWidgets.QLabel())
                self.addWidget(My_and_OU_Message(text, time, type_m))
            elif type_m == "OU":
                self.addWidget(My_and_OU_Message(text, time, type_m))
                self.addWidget(QtWidgets.QLabel())

    def __init__(self):
        super().__init__()

        for i in range(3):
            self.addWidget(QtWidgets.QLabel())

    def addMyMessage(self, text, time):
        Hbox = QtWidgets.QWidget()
        Hbox.setLayout(self.MesContainer(text, "my", time))
        self.addWidget(Hbox)

    def addOtherMessage(self, text, time):
        Hbox = QtWidgets.QWidget()
        Hbox.setLayout(self.MesContainer(text, "OU", time))
        self.addWidget(Hbox)
