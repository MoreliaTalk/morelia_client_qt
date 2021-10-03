import sys
from os import path
from PyQt5.QtWidgets import QApplication, QMainWindow
from interfaces.main_window import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.theme = "dark"
        self.theme_colors = dict()

        if self.theme == "dark":
            self.theme_colors["primary_color"] = "#00ff00"
            self.theme_colors["secondary_color"] = "#fde910"
            self.theme_colors["background_color"] = "#161616"
        
        text_css = open(path.join("styles", "styles.css"), "r").read()

        text_css = text_css.replace("--primary_color", self.theme_colors["primary_color"])
        text_css = text_css.replace("--secondary_color", self.theme_colors["secondary_color"])
        text_css = text_css.replace("--background_color", self.theme_colors["background_color"])

        self.setStyleSheet(text_css)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())