import unittest
from PIL import Image
from PySide6.QtTest import QTest
from PySide6 import QtCore

import main
from tests import lib_for_tests


class TestChatItem(unittest.TestCase):
    def setUp(self) -> None:
        self.app = lib_for_tests.create_qapplication()
        self.mainWindow = main.MainWindow(self.app)

    def test_add_chat_nickname(self):
        count = self.mainWindow.ContactsContent.count() + 1
        self.mainWindow.ChatsController.add_chat(
            "1", "Vasya", "Hello!"
        )
        self.assertEqual(
            self.mainWindow.ChatsController.list_chats[-1].ChatNameLabel.text(), "Vasya"
        )
        self.assertEqual(
            self.mainWindow.ChatsController.list_chats[-1].ChatLastMessageLabel.text(),
            "Hello!"
        )
        self.assertEqual(
            self.mainWindow.ChatsController.list_chats[-1].ContactAvatar.text(),
            "Va"
        )
        self.assertEqual(self.mainWindow.ContactsContent.count(), count)

    def test_test_add_chat_first_and_second_name(self):
        count = self.mainWindow.ContactsContent.count() + 1
        self.mainWindow.ChatsController.add_chat(
            uuid="1",
            chatName="Vasya Pupkin",
            lastMessageText="Hello!"
        )
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
        self.assertEqual(self.mainWindow.ContactsContent.count(), count)

    def test_add_chat_with_image(self):
        count = self.mainWindow.ContactsContent.count() + 1

        image = Image.open("./tests/image_for_test/cat.jpg")

        self.mainWindow.ChatsController.add_chat(
            uuid="1",
            chatName="Vasya",
            lastMessageText="Hello!",
            image=image
        )

        image.close()

        self.assertEqual(
            self.mainWindow.ChatsController.list_chats[-1].ChatNameLabel.text(),
            "Vasya"
        )
        self.assertEqual(
            self.mainWindow.ChatsController.list_chats[-1].ChatLastMessageLabel.text(),
            "Hello!"
        )
        self.assertEqual(self.mainWindow.ContactsContent.count(), count)

    def test_add_chat_blank_name(self):
        self.mainWindow.ChatsController.add_chat(
            uuid="1",
            chatName="",
            lastMessageText="Hello!",
        )

    def test_click_on_chat(self):
        def func_connected_to_signal(chat):
            with self.subTest(chat):
                self.assertIsNotNone(chat)

        new_chat = self.mainWindow.ChatsController.add_chat(
            uuid="1",
            chatName="Vasya Pupkin",

            lastMessageText="Hello!"
        )

        self.mainWindow.ChatsController.signals.selected_chat.connect(func_connected_to_signal)
        QTest.mouseClick(new_chat, QtCore.Qt.MouseButton.LeftButton)


if __name__ == "__main__":
    unittest.main()
