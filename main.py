import sys
from os import path

import sass

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QSizePolicy

from interfaces.main_window import Ui_MainWindow
from modules.MessageElement import MessageElement


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

        self.add_message("my", "11111111111111111111111\n111111111111111111")
    
    def add_message(self, type: str, text: str):
        new_message = MessageElement()
        new_message.setText(text)
        new_message.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        
        if type == "my":
            new_message.setObjectName("myMessage")

            self.MessageAreaContentLayout.addWidget(QLabel())
            self.MessageAreaContentLayout.addWidget(new_message)

        elif type == "other_user":
            new_message.setObjectName("otherUserMessage")

            self.MessageAreaContentLayout.addWidget(new_message)
            self.MessageAreaContentLayout.addWidget(QLabel())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())