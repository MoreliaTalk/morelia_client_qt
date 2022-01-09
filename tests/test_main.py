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

    def test_color_theme(self):
        self.assertEqual(
            self.mainWindow.set_color_theme(),
            self.mainWindow.styleSheet()
        )


if __name__ == "__main__":
    unittest.main()
