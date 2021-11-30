from PySide6.QtWidgets import QApplication
import sys

from main import MainWindow


app = QApplication(sys.argv)
window = MainWindow(app)
window.show()
sys.exit(app.exec())
