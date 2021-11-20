from typing import List
from PyQt5.QtWidgets import QGridLayout, QLabel, QMainWindow, QSizePolicy, QWidget
from loguru import logger


class MessageItem(QLabel):
    def __init__(self):
        super().__init__()


class MessageController:
    def __init__(self, MainWindow, MessageAreaContentLayout):
        super().__init__()

        self.MessageAreaContentLayout: QGridLayout = MessageAreaContentLayout
        self.MainWindow = MainWindow

    def load_messages_current_chat(self, chat_uuid: str):
        self._clear()
        list_messages = list(self.MainWindow.db.list_messages(
            self.MainWindow.db.get_flow_id_by_uuid(chat_uuid)
            ))
        for message in list_messages:
            self._add_message("my", message.text)

    def _clear(self):
        messages = self.MessageAreaContentLayout.parentWidget().findChildren(MessageItem)
        messages: List[MessageItem]
        for mes in messages:
            mes.deleteLater()

        logger.info(f"clear MessagePole")

    def _add_message(self, type: str, text: str):
        new_message = MessageItem()
        new_message.setText(text)
        new_message.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)

        if type == "my":
            new_message.setObjectName("myMessage")

            self.MessageAreaContentLayout.addWidget(QLabel())
            self.MessageAreaContentLayout.addWidget(new_message)

        elif type == "other_user":
            new_message.setObjectName("otherUserMessage")

            self.MessageAreaContentLayout.addWidget(new_message)
            self.MessageAreaContentLayout.addWidget(QLabel())

        else:
            return False

        logger.info(f"add new message type: {type} text: {text}")

        return new_message
