import sys
from os import path

import sass

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from interfaces.main_window import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        """
        self.theme = "dark"
        self.theme_colors = dict()
        if self.theme == "dark":
            self.theme_colors["primary_color"] = "#00ff00"
            self.theme_colors["secondary_color"] = "#fde910"
            self.theme_colors["background_color"] = "#161616"
        """
        
        text_css = open(path.join("scss", "styles.scss"), "r").read()

        text_css = sass.compile(string=text_css)

        print(text_css)

        self.setStyleSheet(text_css)
    
    # TODO Сделать добавление сообщений в чат
    # def add_message(self, text: str, time):
        # self.MessageAreaContentLayout.addChildWidget()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())