from os import path
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
from random import randrange

class ContactCard(QtWidgets.QWidget):
    def __init__(self, contactName, lastMessageText, img):
        super(ContactCard, self).__init__()
        uic.loadUi(path.join("interfaces", "ui", "contact_card.ui"), self)
        self.ChatNameLabel.setText(contactName)
        self.ChatLastMessageLabel.setText(lastMessageText)
        if img:
            picture = path.join("interfaces", "ui", img)
            self.ContactAvatar.setPixmap(QPixmap(picture))
        else:
            namesWord = contactName.split(" ")
            self.ContactAvatar.setText(namesWord[0][0] + namesWord[1][0])
            self.ContactAvatar.setStyleSheet(f"background-color: rgb({randrange(100)},{randrange(100)},{randrange(100)}); ")
