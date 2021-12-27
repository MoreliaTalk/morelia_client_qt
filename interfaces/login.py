import sys
from collections import namedtuple
from PySide6.QtGui import QShortcut, QKeySequence

from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QWidget

from interfaces.raw.login_dialog import Ui_loginDialog
from interfaces.helpers import load_font, set_color_theme

from loguru import logger
from modules.logging import set_logger_setting


set_logger_setting()


def is_filled(line_edit: QLineEdit) -> bool:
    """Check if text property filled,
    if not add dynamic property "wrongInput" for redraw style,
    and invoke redraw_widget() for apply style changes
    args:
        line_edit - QLineEdit object
    return: bool
        Is text property filled
    """
    PARAM_NAME = "wrongInput"
    if line_edit.text() == "":
        line_edit.setProperty(PARAM_NAME, True)
        redraw_widget(line_edit)
        return False
    else:
        line_edit.setProperty(PARAM_NAME, False)
        redraw_widget(line_edit)
        return True


def redraw_widget(widget: QWidget) -> None:
    """Helper for redraw stylesheet of any QWidget
    args:
        widget - QWidget object
    return: None
    """
    widget.style().unpolish(widget)
    widget.style().polish(widget)
    widget.update()


class LoginDialog(Ui_loginDialog, QDialog):
    def __init__(self, app: QApplication, login="", password=""):
        super().__init__()
        self.app = app

        self.action = "Cancel"
        logger.info("Login dialog")

        self.setupUi(self)
#        load_font()
#        set_color_theme(self)
        self.loginLineEdit.setText(login)
        self.passwordLineEdit.setText(password)
        self.cancelPushButton.clicked.connect(self.cancel_form)
        self.okPushButton.clicked.connect(self.accept_form)
        self.shortcut = QShortcut(QKeySequence("Esc"), self)
        self.shortcut.activated.connect(self.cancel_form)

    def cancel_form(self) -> None:
        self.close()

    def accept_form(self) -> None:
        if self.loginTabWidget.currentWidget().objectName() == "signInTab":
            if is_filled(self.loginLineEdit) and is_filled(self.passwordLineEdit):
                self.action = "Login"
                self.close()
        if self.loginTabWidget.currentWidget().objectName() == "registerTab":
            if is_filled(self.loginNameLineEdit) and \
                    is_filled(self.passwordRegisterLineEdit) and \
                    is_filled(self.displayNameLineEdit) and \
                    is_filled(self.eMailLineEdit):
                self.action = "Register"
                self.close()

    def return_result(self) -> namedtuple:
        """Used to get input result after dialog closing
        return:
            Result: namedtuple
                .action = ("Cancel", "Login", "Register")
                .login: string login name (Register and Login mode)
                .password: string (Register and Login mode)
                .username: string Real name or display name (only in Register mode)
                .email: string (only in Register mode)
        """
        Result = namedtuple("Result", "action login password username email")
        if self.action == "Login":
            return Result(self.action, self.loginLineEdit.text(),
                          self.passwordLineEdit.text(),
                          "", "")
        elif self.action == "Register":
            return Result(self.action, self.loginNameLineEdit.text(),
                          self.passwordRegisterLineEdit.text(),
                          self.displayNameLineEdit.text(),
                          self.eMailLineEdit.text())
        else:
            return Result(self.action, "", "", "", "")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LoginDialog(app)
    login.exec()
    logger.info("Dialog result: "+login.return_result().action)
