import unittest
import sys
from PyQt5.QtWidgets import QApplication

import main


class TestAddMessage(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.mainWindow = main.MainWindow()

    def test_add_my_message(self):
        self.assertEqual(self.mainWindow.MessageController.add_message(
                            type="my", text="111111"
                        ),
                         self.mainWindow.MessageAreaContent.children()[-1])

    def test_add_other_user_message(self):
        self.assertEqual(self.mainWindow.MessageController.add_message(
                            type="other_user", text="111111"
                        ),
                         self.mainWindow.MessageAreaContent.children()[-2])

    def test_add_not_correct_type_message(self):
        self.assertFalse(self.mainWindow.MessageController.add_message(
                            type=")))", text="111111"
                        ))


if __name__ == "__main__":
    unittest.main()
