from os import path

import sass

from PyQt5.QtWidgets import QMainWindow

from interfaces.raw.main_window import Ui_MainWindow
from interfaces.chats_controller import ChatsController
from interfaces.message_controller import MessageController

from loguru import logger
from modules.logging import set_logger_setting
from modules.database.clientdb import ClientDb

set_logger_setting()


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()

        logger.info("Start client")

        self.setupUi(self)
        self.setColorTheme()
        self.connect_to_db()

        self.MessageController = MessageController(self.MessageAreaContentLayout)
        self.ChatsController = ChatsController(self.ContactsContent)

    def connect_to_db(self):
        self.db = ClientDb()
        if not self.db.check_db_tables_created():
            self.db.create_db()

    def setColorTheme(self, primary_color: str = None,
                      secondary_color: str = None,
                      background_color: str = None):

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
