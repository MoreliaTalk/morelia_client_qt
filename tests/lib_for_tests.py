import sys

from PySide6.QtWidgets import QApplication


def create_qapplication():
    if QApplication.instance():
        return QApplication.instance()
    else:
        return QApplication(sys.argv)



