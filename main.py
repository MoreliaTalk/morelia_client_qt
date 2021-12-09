from os import path
from pathlib import Path
from uuid import uuid4

import typing
from PySide6.QtGui import QFont, QFontDatabase
import sass

from PySide6.QtWidgets import QApplication, QMainWindow

from interfaces.raw.main_window import Ui_MainWindow
from interfaces.chats_controller import ChatsController
from interfaces.message_controller import MessageController

from loguru import logger
from modules.logging import set_logger_setting
from modules.database.clientdb import ClientDb
from modules.database import models

set_logger_setting()


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, app: QApplication):
        super().__init__()
        self.app = app

        logger.info("Start client")

        self.setupUi(self)
        self.setWindowTitle("MoreliaTalk")
        self.load_font()
        self.setColorTheme()
        self.connect_to_db()

        self.MessageController = MessageController(self, self.MessageAreaContentLayout)
        self.ChatsController = ChatsController(self.ContactsContent)
        self.load_flow_and_mes()

        self.ChatsController.signals.selected_chat.connect(
            lambda chat: self.MessageController.load_messages_current_chat(chat.uuid)
        )

    def load_flow_and_mes(self):
        list_flow: typing.List[models.Flow] = self.db.list_flow()
        for flow in list_flow:
            lastMessage = self.db.get_last_message(flow.uuid)
            lastMessageText = lastMessage.text if lastMessage else "Здесь пока нет сообщений"
            self.ChatsController.add_chat(
                uuid=flow.uuid,
                chatName=flow.title,
                lastMessageText=lastMessageText
            )

    def connect_to_db(self):
        self.db = ClientDb()
        if not self.db.check_db_tables_created():
            self.db.create_db()

    def load_font(self):
        fonts_dict = {
            "Roboto": (
                "Black",
                "BlackItalic",
                "Bold",
                "BoldItalic",
                "Italic",
                "Light",
                "LightItalic",
                "Medium",
                "Regular",
                "Thin",
                "ThinItalic"
            )
        }
        for font_family in fonts_dict:
            for font in font_family:
                QFontDatabase.addApplicationFont(str(Path.cwd() / "fonts" / f"{font}.ttf"))

    def setColorTheme(self, primary_color: str = None,
                      secondary_color: str = None,
                      background_color: str = None):
        self.app.setStyle("fusion")
        self.app.setFont(QFont("Roboto", 10))

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
