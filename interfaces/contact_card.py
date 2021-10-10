from os import path
from random import randrange
from PyQt5 import QtWidgets, uic


class ContactCard(QtWidgets.QWidget):
    def __init__(self, contactName, lastMessageText):
        super(ContactCard, self).__init__()
        uic.loadUi(path.join("interfaces", "ui", "contact_card.ui"), self)
        namesWord = contactName.split(" ")
        self.ChatNameLabel.setText(contactName)
        self.ChatLastMessageLabel.setText(lastMessageText)
        self.ContactAvatar.setText(namesWord[0][0] + namesWord[1][0])
        self.ContactAvatar.setStyleSheet(f"background-color: rgb({randrange(100)},{randrange(100)},{randrange(100)}); ")
