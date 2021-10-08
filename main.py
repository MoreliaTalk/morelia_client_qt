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
        self.MessageController = MessageController(self.MessageAreaContentLayout)

    def setColorTheme(self, primary_color: str = "#00ff00",
                      secondary_color: str = "#fde910",
                      background_color: str = "#161616"):
        text_css = open(path.join("scss", "styles.scss"), "r").read()

        if not (primary_color == "#00ff00" and
                secondary_color == "#fde910" and
                background_color == "#161616"):
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
