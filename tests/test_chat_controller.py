import unittest
import sys
from PyQt5.QtWidgets import QApplication

import main


class TestAddChat(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.mainWindow = main.MainWindow()

    def test_add_chat(self):
        self.assertEqual(self.mainWindow.ChatsController.add_chat(
                            contactName="Test Chat",
                            lastMessageText="Last message in test chat",
                            imgPath=""
                        ), self.mainWindow.ContactsContent.itemAt(self.mainWindow.ContactsContent.count()-1).widget())

    def test_chats_count(self):
        self.assertEqual(self.mainWindow.ContactsContent.count(), 0)


if __name__ == "__main__":
    unittest.main()
