from os import path
import random

from PIL import Image, ImageDraw, ImageOps
from PIL.ImageQt import ImageQt

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap, QPainter, QPainterPath

from .raw_interfaces.contact_card import Ui_ContactCard


class ChatItem(Ui_ContactCard, QtWidgets.QWidget):
    def __init__(self, chatName: str, lastMessageText: str, image: Image.Image = None):
        super().__init__()

        self.setupUi(self)

        self.ChatNameLabel.setText(chatName)
        self.ChatLastMessageLabel.setText(lastMessageText)

        if image:
            image_result = image.convert("RGBA")
            image_result = image_result.resize(
                [
                    self.ContactAvatar.width(),
                    self.ContactAvatar.height()
                ]
            )

            big_size = (image_result.size[0]*3, image_result.size[0]*3)
            mask = Image.new("L", big_size)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + big_size, fill=255)
            mask = mask.resize(image_result.size, Image.ANTIALIAS)
            image_result.putalpha(mask)

            image_result_qt = ImageQt(image_result)

            self.ContactAvatar.setPixmap(QPixmap(QImage(image_result_qt)))
        else:
            splitName = chatName.split()

            if len(splitName) == 1:
                self.ContactAvatar.setText(splitName[0][0]+splitName[0][1])
            elif len(splitName) == 2:
                self.ContactAvatar.setText(splitName[0][0]+splitName[1][0])

            randomColor =  f"hsl( { random.randint(190, 360) }, 100%, 50% )"
            self.ContactAvatar.setStyleSheet(
                f"background-color: { randomColor }"
            )



class ChatsController:
    def __init__(self, ChatsContentLayout):
        super().__init__()
        self.ChatsContentLayout = ChatsContentLayout

    def add_chat(self, chatName: str, lastMessageText: str, image: Image.Image = None):
        new_chat_item = ChatItem(chatName, lastMessageText, image)
        self.ChatsContentLayout.addWidget(new_chat_item)

"""        
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
"""


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    widget = ChatItem("Nekrod", "Hello!")
    # , QImage(100, 100, QImage.Format.Format_RGB16)
    widget.show()
    sys.exit(app.exec_())
