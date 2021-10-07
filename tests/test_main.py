import unittest
import sys
from PyQt5.QtWidgets import QApplication

import main


class TestMainWindow(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.mainWindow = main.MainWindow()
        self.mainWindow.show()
        
    def test_add_message(self):
        self.assertTrue(self.mainWindow.add_message(type="my", text="111111"))


if __name__ == "__main__":
    unittest.main()