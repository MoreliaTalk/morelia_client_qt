import random

from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt

from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage, QPixmap

from .raw.contact_card import Ui_ContactCard


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

            big_size = (image_result.size[0]*4, image_result.size[0]*4)
            mask = Image.new("L", big_size)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + big_size, fill=255)
            mask = mask.resize(image_result.size, Image.ANTIALIAS)
            image_result.putalpha(mask)

            image_result_qt = ImageQt(image_result)

            self.ContactAvatar.setPixmap(QPixmap(QImage(image_result_qt)))
        else:
            splitName = chatName.split()
            name_initials = str()

            if len(splitName) == 0:
                name_initials = "o_O"
            elif len(splitName) == 1:
                name_initials = splitName[0][0:2]
            elif len(splitName) >= 2:
                for i in splitName:
                    name_initials += i[0]

            self.ContactAvatar.setText(name_initials)

            randomColor = f"hsl( { random.randint(190, 360) }, 100%, 50% )"
            self.ContactAvatar.setStyleSheet(
                f"background-color: { randomColor }"
            )


class ChatsController:
    def __init__(self, ChatsContentLayout: QtWidgets.QLayout):
        self.ChatsContentLayout = ChatsContentLayout
        self.list_chats: list[ChatItem] = list()

    def add_chat(self, chatName: str, lastMessageText: str, image: Image.Image = None):
        new_chat_item = ChatItem(chatName, lastMessageText, image)
        self.list_chats.append(new_chat_item)
        self.ChatsContentLayout.addWidget(new_chat_item)
