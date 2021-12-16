import unittest
import sys
import random
from PySide6.QtWidgets import QApplication

import main
from tests import lib_for_tests


class TestSetColorTheme(unittest.TestCase):
    def setUp(self):
        self.app = lib_for_tests.create_qapplication()
        self.mainWindow = main.MainWindow(self.app)
    
    def test_standart_color_theme(self):
        self.assertEqual(self.mainWindow.set_color_theme(), self.mainWindow.styleSheet())

    def test_custom_color_theme(self):
        self.assertEqual(
            self.mainWindow.set_color_theme(
                primary_color="#{:06x}".format(random.randint(0, 0xFFFFFF)),
                secondary_color="#{:06x}".format(random.randint(0, 0xFFFFFF)),
                background_color="#{:06x}".format(random.randint(0, 0xFFFFFF))
            ),
            self.mainWindow.styleSheet()
        )


if __name__ == "__main__":
    unittest.main()
