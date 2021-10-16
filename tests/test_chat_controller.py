import unittest
import sys
from PIL import Image
from PyQt5.QtWidgets import QApplication

import main

class TestAddChatItem(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.mainWindow = main.MainWindow()

    def test_add_chat_nikname(self):
        count_up_to = self.mainWindow.ContactsContent.count()
        self.mainWindow.ChatsController.add_chat("Vasya", "Hello!")
        self.assertEqual(
            self.mainWindow.ChatsController.list_chats[-1].ChatNameLabel.text(),
            "Vasya"
        )
        self.assertEqual(
            self.mainWindow.ChatsController.list_chats[-1].ChatLastMessageLabel.text(),
            "Hello!"
        )
        self.assertEqual(
            self.mainWindow.ChatsController.list_chats[-1].ContactAvatar.text(),
            "Va"
        )
        self.assertEqual(self.mainWindow.ContactsContent.count(), count_up_to+1)

    def test_test_add_chat_first_and_second_name(self):
        count_up_to = self.mainWindow.ContactsContent.count()
        self.mainWindow.ChatsController.add_chat("Vasya Pupkin", "Hello!")
        self.assertEqual(
            self.mainWindow.ChatsController.list_chats[-1].ChatNameLabel.text(),
            "Vasya Pupkin"
        )
        self.assertEqual(
            self.mainWindow.ChatsController.list_chats[-1].ChatLastMessageLabel.text(),
            "Hello!"
        )
        self.assertEqual(
            self.mainWindow.ChatsController.list_chats[-1].ContactAvatar.text(),
            "VP"
        )
        self.assertEqual(self.mainWindow.ContactsContent.count(), count_up_to+1)

    def test_add_chat_with_image(self):
        count_up_to = self.mainWindow.ContactsContent.count()
        self.mainWindow.ChatsController.add_chat(
            "Vasya",
            "Hello!",
            Image.open("./tests/image_for_test/cat.jpg")
        )
        self.assertEqual(
            self.mainWindow.ChatsController.list_chats[-1].ChatNameLabel.text(),
            "Vasya"
        )
        self.assertEqual(
            self.mainWindow.ChatsController.list_chats[-1].ChatLastMessageLabel.text(),
            "Hello!"
        )
        self.assertEqual(self.mainWindow.ContactsContent.count(), count_up_to+1)

        


if __name__ == "__main__":
    unittest.main()
