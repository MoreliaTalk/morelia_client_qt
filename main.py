import sys
from os import path

import sass

from PyQt5.QtWidgets import QApplication, QMainWindow

from interfaces.main_window import Ui_MainWindow
from modules.message_controller import MessageController


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setColorTheme()

        self.MessageController = MessageController(self.MessageAreaContentLayout)

    def setColorTheme(self, primary_color: str = "#00ff00",
                      secondary_color: str = "#fde910",
                      background_color: str = "#161616"):

        file = open(path.join("scss", "styles.scss"), "r")
        text_css = file.read()
        file.close()

        if not (primary_color == (default_args_value := self.setColorTheme.__defaults__)[0] and
                secondary_color == default_args_value and
                background_color == default_args_value):
            text_css.replace("#00ff00", primary_color)
            text_css.replace("#fde910", secondary_color)
            text_css.replace("#161616", background_color)

        text_css = sass.compile(string=text_css)
        self.setStyleSheet(text_css)

        return text_css


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
