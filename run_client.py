from PySide6.QtWidgets import QApplication
import sys

from main import MainWindow
from interfaces.login import LoginDialog


app = QApplication(sys.argv)
login = LoginDialog(app)
login.exec()
window = MainWindow(app)
window.show()
sys.exit(app.exec())
