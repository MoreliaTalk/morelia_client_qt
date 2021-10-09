import unittest
import sys
import random
from PyQt5.QtWidgets import QApplication

import main


class TestSetColorTheme(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.mainWindow = main.MainWindow()

    def test_standart_color_theme(self):
        self.assertEqual(self.mainWindow.setColorTheme(), self.mainWindow.styleSheet())

    def test_custom_color_theme(self):
        self.assertEqual(self.mainWindow.setColorTheme(
                            primary_color="#{:06x}".format(random.randint(0, 0xFFFFFF)),
                            secondary_color="#{:06x}".format(random.randint(0, 0xFFFFFF)),
                            background_color="#{:06x}".format(random.randint(0, 0xFFFFFF))
                        ),
                         self.mainWindow.styleSheet())


if __name__ == "__main__":
    unittest.main()
