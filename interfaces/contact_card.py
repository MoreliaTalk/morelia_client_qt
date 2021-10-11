from os import path
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath
from random import randrange


class ContactCard(QtWidgets.QWidget):
    def __init__(self, contactName, lastMessageText, img):
        super(ContactCard, self).__init__()
        uic.loadUi(path.join("interfaces", "ui", "contact_card.ui"), self)
        self.ChatNameLabel.setText(contactName)
        self.ChatLastMessageLabel.setText(lastMessageText)
        if img:
            labelSize = self.ContactAvatar.width()
            sourcePixmap = QPixmap(path.join("interfaces", "ui", img))
            imgSize = min(sourcePixmap.width(), sourcePixmap.height())
            croppedPixmap = sourcePixmap.copy((sourcePixmap.width()-imgSize)/2,
                                              (sourcePixmap.height()-imgSize)/2,
                                              imgSize, imgSize)
            smallerPixmap = croppedPixmap.scaled(labelSize, labelSize, transformMode=Qt.SmoothTransformation)
            self.ContactAvatar.radius = self.ContactAvatar.width()/2
            self.ContactAvatar.target = QPixmap(labelSize, labelSize)
            self.ContactAvatar.target.fill(Qt.transparent)
            painter = QPainter(self.ContactAvatar.target)
            painter.setRenderHint(QPainter.Antialiasing, True)
            painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
            painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
            painterPath = QPainterPath()
            painterPath.addRoundedRect(
                0, 0, labelSize, labelSize,
                labelSize/2, labelSize/2)
            painter.setClipPath(painterPath)
            painter.drawPixmap(0, 0, smallerPixmap)
            self.ContactAvatar.setPixmap(self.ContactAvatar.target)
        else:
            namesWord = contactName.split(" ")
            self.ContactAvatar.setText(namesWord[0][0] + namesWord[1][0])
            self.ContactAvatar.setStyleSheet(f"background-color: rgb({randrange(100)},{randrange(100)},{randrange(100)}); ")
