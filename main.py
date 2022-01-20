import os
from os import path
from pathlib import Path

from PySide6.QtGui import QFont, QFontDatabase, QIcon
import sass

from PySide6.QtWidgets import QApplication, QMainWindow

from interfaces.raw.main_window import Ui_MainWindow
from interfaces.chats_controller import ChatsController
from interfaces.message_controller import MessageController

from loguru import logger

from interfaces.settings_dialog import SettingsDialog
from modules.logging import set_logger_setting
from modules.database.clientdb import ClientDb
from modules import default_colors

set_logger_setting()


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self, app: QApplication):
        super().__init__()
        self.app = app

        logger.info("Start client")

        self.setupUi(self)
        self.setWindowTitle("MoreliaTalk")
        self.load_font()

        self.db = ClientDb()
        self.db.create_db()

        self.set_color_theme()

        self.ChatsController = ChatsController(self.ContactsContent)
        self.MessageController = MessageController(self.db, self.ChatsController, self.MessageAreaContentLayout)
        self.load_flow_and_mes()

        self.ChatsController.signals.selected_chat.connect(
            lambda chat: self.MessageController.load_messages_current_chat(chat.uuid)
        )

        self.SettingsDialog = SettingsDialog(
            parent=self,
            db=self.db
        )

        self.MenuButton.clicked.connect(self.SettingsDialog.exec)

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

    def set_color_theme(self):
        self.app.setStyle("fusion")
        self.app.setFont(QFont("Roboto", 10))

        self.MenuButton.setIcon(QIcon(
            "./icons/menu-line.png"
        ))

        file = open(path.join("scss", "styles.scss"), "r")
        text_css = file.read()
        file.close()

        if primary_color := self.db.get_param("primary_color"):
            text_css = text_css.replace(default_colors.PRIMARY_COLOR, primary_color)
        else:
            self.db.set_param("primary_color", default_colors.PRIMARY_COLOR)

        if secondary_color := self.db.get_param("secondary_color"):
            text_css = text_css.replace(default_colors.SECONDARY_COLOR, secondary_color)
        else:
            self.db.set_param("secondary_color", default_colors.SECONDARY_COLOR)

        if background_color := self.db.get_param("background_color"):
            text_css = text_css.replace(default_colors.BACKGROUND_COLOR, background_color)
        else:
            self.db.set_param("background_color", default_colors.BACKGROUND_COLOR)

        text_css = sass.compile(string=text_css)
        self.setStyleSheet(text_css)
        logger.info("set color theme")

        return text_css
