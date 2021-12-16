import unittest
import sys
from PySide6.QtWidgets import QApplication

import main
from interfaces.message_controller import MessageItem
from tests import lib_for_tests


class TestAddMessage(unittest.TestCase):
    def setUp(self) -> None:
        self.app = lib_for_tests.create_qapplication()
        self.mainWindow = main.MainWindow(self.app)
        
    def test_add_my_message(self):
        message = self.mainWindow.MessageController._add_message(
            mes_type="my", mes_text="111111"
        )
        self.assertEqual(message, self.mainWindow.MessageAreaContent.findChildren(MessageItem)[-1])

    def test_add_other_user_message(self):
        message = self.mainWindow.MessageController._add_message(
            mes_type="other_user", mes_text="111111"
        )
        self.assertEqual(message, self.mainWindow.MessageAreaContent.findChildren(MessageItem)[-1])

    def test_add_not_correct_mes_type_message(self):
        self.assertFalse(self.mainWindow.MessageController._add_message(
                            mes_type=")))", mes_text="111111"
                        ))


if __name__ == "__main__":
    unittest.main()
