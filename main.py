import os
from os import path
from pathlib import Path

from PIL.ImageQt import ImageQt
from PIL import Image
from PySide6.QtCore import QSize
from PySide6.QtGui import QFont, QFontDatabase, QPixmap, QIcon, QImage
import sass

from PySide6.QtWidgets import QApplication, QMainWindow

from interfaces.raw.main_window import Ui_MainWindow
from interfaces.chats_controller import ChatsController
from interfaces.message_controller import MessageController

from loguru import logger
from modules.logging import set_logger_setting
from modules.database.clientdb import ClientDb

set_logger_setting()


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, app: QApplication):
        super().__init__()
        self.app = app

        logger.info("Start client")

        self.setupUi(self)
        self.setWindowTitle("MoreliaTalk")
        self.load_font()
        self.set_color_theme()

        self.db = ClientDb()
        self.db.create_db()

        self.ChatsController = ChatsController(self.ContactsContent)
        self.MessageController = MessageController(self.db, self.ChatsController, self.MessageAreaContentLayout)
        self.load_flow_and_mes()

        self.ChatsController.signals.selected_chat.connect(
            lambda chat: self.MessageController.load_messages_current_chat(chat.uuid)
        )

    def load_flow_and_mes(self):
        list_flow = self.db.list_flow()
        for flow in list_flow:
            last_message_text = flow.last_message if flow.last_message else "Здесь пока нет сообщений"
            self.ChatsController.add_chat(
                uuid=flow.uuid,
                chatName=flow.title,
                lastMessageText=last_message_text
            )

    @staticmethod
    def load_font():
        fonts_list = tuple(os.walk(Path.cwd() / "fonts"))[0][-1]
        for font in fonts_list:
            QFontDatabase.addApplicationFont(str(Path.cwd() / "fonts" / font))

    def set_color_theme(self, primary_color: str = None,
                        secondary_color: str = None,
                        background_color: str = None):
        self.app.setStyle("fusion")
        self.app.setFont(QFont("Roboto", 10))

        self.MenuButton.setIcon(QIcon(
            "./icons/menu-line.png"
        ))

        file = open(path.join("scss", "styles.scss"), "r")
        text_css = file.read()
        file.close()
        custom_theme = False

        if primary_color:
            text_css = text_css.replace("#00ff00", primary_color)
            custom_theme = True

        if secondary_color:
            text_css = text_css.replace("#fde910", secondary_color)
            custom_theme = True

        if background_color:
            text_css = text_css.replace("#161616", background_color)
            custom_theme = True

        text_css = sass.compile(string=text_css)
        self.setStyleSheet(text_css)

        if custom_theme:
            logger.info("set custom color theme")
            logger.info(f"primary color: {primary_color}")
            logger.info(f"secondary color: {secondary_color}")
            logger.info(f"background color: {background_color}")
        else:
            logger.info("set standart color theme")

        return text_css
