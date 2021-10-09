from os import path

import sass

from PyQt5.QtWidgets import QMainWindow

from interfaces.main_window import Ui_MainWindow
from modules.message_controller import MessageController


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.setColorTheme()
        self.MessageController = MessageController(self.MessageAreaContentLayout)

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
