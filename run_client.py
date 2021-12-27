from PySide6.QtWidgets import QApplication
import sys

from main import MainWindow
from interfaces.login import LoginDialog


app = QApplication(sys.argv)
window = MainWindow(app)
window.show()
sys.exit(app.exec())
