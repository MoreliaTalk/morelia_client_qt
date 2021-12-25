from os import path
from pathlib import Path
from PySide6.QtGui import QFont, QFontDatabase
import sass

from PySide6.QtWidgets import QApplication, QDialog

from interfaces.raw.login_dialog import Ui_loginDialog

from loguru import logger
from modules.logging import set_logger_setting


class LoginDialog(Ui_loginDialog, QDialog):
    def __init__(self, app: QApplication):
        super().__init__()
        self.app = app

        logger.info("Login dialog")

        self.setupUi(self)
        self.load_font()
        self.set_color_theme()


    @staticmethod
    def load_font():
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

    def set_color_theme(self, primary_color: str = None,
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
