# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 450, 30))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ExitButton = QtWidgets.QPushButton(self.frame)
        self.ExitButton.setEnabled(True)
        self.ExitButton.setGeometry(QtCore.QRect(405, 0, 45, 30))
        self.ExitButton.setAutoFillBackground(False)
        self.ExitButton.setText("")
        self.ExitButton.setAutoDefault(False)
        self.ExitButton.setDefault(False)
        self.ExitButton.setFlat(False)
        self.ExitButton.setObjectName("ExitButton")
        self.MinimazeButton = QtWidgets.QPushButton(self.frame)
        self.MinimazeButton.setEnabled(True)
        self.MinimazeButton.setGeometry(QtCore.QRect(360, 0, 45, 30))
        self.MinimazeButton.setAutoFillBackground(False)
        self.MinimazeButton.setText("")
        self.MinimazeButton.setAutoDefault(False)
        self.MinimazeButton.setDefault(False)
        self.MinimazeButton.setFlat(False)
        self.MinimazeButton.setObjectName("MinimazeButton")
        self.LabelMT = QtWidgets.QLabel(self.frame)
        self.LabelMT.setGeometry(QtCore.QRect(120, 0, 210, 25))
        font = QtGui.QFont()
        font.setFamily("Ustroke")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.LabelMT.setFont(font)
        self.LabelMT.setObjectName("LabelMT")
        self.MessagePole = QtWidgets.QScrollArea(self.centralwidget)
        self.MessagePole.setGeometry(QtCore.QRect(0, 30, 450, 500))
        self.MessagePole.setWidgetResizable(True)
        self.MessagePole.setObjectName("MessagePole")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 448, 498))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.MessagePole.setWidget(self.scrollAreaWidgetContents)
        self.SendButton = QtWidgets.QPushButton(self.centralwidget)
        self.SendButton.setGeometry(QtCore.QRect(360, 530, 90, 70))
        self.SendButton.setObjectName("SendButton")
        self.InputText = QtWidgets.QTextEdit(self.centralwidget)
        self.InputText.setGeometry(QtCore.QRect(0, 530, 360, 70))
        self.InputText.setObjectName("InputText")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.LabelMT.setText(_translate("MainWindow", "MoreliaTalk"))
        self.SendButton.setText(_translate("MainWindow", "PushButton"))
