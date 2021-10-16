from os import path

import sass

from PIL import Image

from PyQt5.QtWidgets import QMainWindow

from interfaces.raw_interfaces.main_window import Ui_MainWindow
from interfaces.chats_controller import ChatsController
from interfaces.message_controller import MessageController


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()

        # For direct load .UI use: self.ui = uic.loadUi(path.join("interfaces", "ui", "main_window.ui"), self)
        self.setupUi(self)

        self.setColorTheme()
        self.MessageController = MessageController(self.MessageAreaContentLayout)
        self.ChatsController = ChatsController(self.ContactsContent)

        self.ChatsController.add_chat("Nekrod", "hello!", Image.open("./cat.jpg"))

    def setColorTheme(self, primary_color: str = None,
                      secondary_color: str = None,
                      background_color: str = None):

        file = open(path.join("scss", "styles.scss"), "r")
        text_css = file.read()
        file.close()

        if primary_color:
            text_css = text_css.replace("#00ff00", primary_color)

        if secondary_color:
            text_css = text_css.replace("#fde910", secondary_color)

        if background_color:
            text_css = text_css.replace("#161616", background_color)

        print(text_css)
        text_css = sass.compile(string=text_css)
        self.setStyleSheet(text_css)

        return text_css
