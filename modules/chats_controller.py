from os import path
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath
from random import randrange
from interfaces.contact_card import Ui_ContactCard


class ChatsController:
    def __init__(self, ChatsContentLayout):
        super().__init__()
        self.ChatsContentLayout = ChatsContentLayout

    def add_chat(self, contactName, lastMessageText, imgPath):
        new_contact_card = QtWidgets.QWidget()
        ui = Ui_ContactCard()
        ui.setupUi(new_contact_card)

        ui.ChatNameLabel.setText(contactName)
        ui.ChatLastMessageLabel.setText(lastMessageText)
        if imgPath:
            labelSize = ui.ContactAvatar.width()
            sourcePixmap = QPixmap(path.join("interfaces", "ui", imgPath))
            imgSize = min(sourcePixmap.width(), sourcePixmap.height())
            croppedPixmap = sourcePixmap.copy(int((sourcePixmap.width()-imgSize)/2),
                                              int((sourcePixmap.height()-imgSize)/2),
                                              imgSize, imgSize)
            smallerPixmap = croppedPixmap.scaled(labelSize, labelSize, transformMode=Qt.SmoothTransformation)
            ui.ContactAvatar.target = QPixmap(labelSize, labelSize)
            ui.ContactAvatar.target.fill(Qt.transparent)
            painter = QPainter(ui.ContactAvatar.target)
            painter.setRenderHint(QPainter.Antialiasing, True)
            painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
            painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
            painterPath = QPainterPath()
            painterPath.addRoundedRect(
                0, 0, labelSize, labelSize,
                labelSize/2, labelSize/2)
            painter.setClipPath(painterPath)
            painter.drawPixmap(0, 0, smallerPixmap)
            ui.ContactAvatar.setPixmap(ui.ContactAvatar.target)
        else:
            namesWord = contactName.split(" ")
            ui.ContactAvatar.setText(namesWord[0][0] + namesWord[1][0])
            ui.ContactAvatar.setStyleSheet(
                f"background-color: rgb({randrange(100)},{randrange(100)},{randrange(100)});")

        self.ChatsContentLayout.addWidget(new_contact_card)
        return new_contact_card
