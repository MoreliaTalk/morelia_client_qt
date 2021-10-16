from os import path
import random

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPainterPath

from .raw_interfaces.contact_card import Ui_ContactCard


class ChatItem(Ui_ContactCard, QtWidgets.QWidget):
    def __init__(self, chatName: str, lastMessageText: str, image: QImage = None):
        super().__init__()

        self.setupUi(self)

        self.ChatNameLabel.setText(chatName)
        self.ChatLastMessageLabel.setText(lastMessageText)

        if image:
            pass
        else:
            splitName = chatName.split()

            if len(splitName) == 1:
                self.ContactAvatar.setText(splitName[0][0]+splitName[0][1])
            elif len(splitName) == 2:
                self.ContactAvatar.setText(splitName[0][0]+splitName[1][0])

            randomColor =  "#{:06x}".format(random.randint(0, 0xFFFFFF)) 
            self.ContactAvatar.setStyleSheet(
                f"background-color: { randomColor }"
            )



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


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    widget = ChatItem("Nekrod", "Hello!")
    # , QImage(100, 100, QImage.Format.Format_RGB16)
    widget.show()
    sys.exit(app.exec_())
