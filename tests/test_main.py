import unittest
import sys
from PyQt5.QtWidgets import QApplication

import main


class TestSetColorTheme(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.mainWindow = main.MainWindow()

    def test_color_theme(self):
        self.assertEqual(self.mainWindow.setColorTheme(), self.mainWindow.styleSheet())


if __name__ == "__main__":
    unittest.main()
