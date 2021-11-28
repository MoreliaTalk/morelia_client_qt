from typing import List
from PyQt5.QtWidgets import QGridLayout, QLabel, QMainWindow, QSizePolicy, QWidget
from loguru import logger
from .raw.message_card import Ui_MessageCard


class MessageItem(Ui_MessageCard, QWidget):
    def __init__(self, text: str, username: str = None):
        super().__init__()

        self.setupUi(self)

        if username:
            self.usernameLabel.setText(f"<b>{username}<b>")
        else:
            self.usernameLabel.deleteLater()

        self.textLabel.setText(text)


class MessageController:
    def __init__(self, MainWindow, MessageAreaContentLayout):
        super().__init__()

        self.MessageAreaContentLayout: QGridLayout = MessageAreaContentLayout

        for i in range(3):
            self.MessageAreaContentLayout.setColumnStretch(i, 1)

        self.MainWindow = MainWindow

    def load_messages_current_chat(self, chat_uuid: str):
        self._clear()
        list_messages = list(self.MainWindow.db.list_messages(
            self.MainWindow.db.get_flow_id_by_uuid(chat_uuid)
            ))

        if len(list_messages):
            for message in list_messages:
                if message.user_uuid == self.MainWindow.db.get_param("user_uuid"):
                    self._add_message("my", message.text)
                else:
                    if self.MainWindow.db.get_flow(flow_uuid=chat_uuid).flowType == "group":
                        self._add_message("other_user", message.text, message.username)
                    else:
                        self._add_message("other_user", message.text)

        else:
            self._add_message("special", "Здесь пока нет сообщений")

    def _clear(self):
        messages = self.MessageAreaContentLayout.parentWidget().findChildren(MessageItem)
        messages: List[MessageItem]
        for mes in messages:
            mes.deleteLater()

        logger.info("clear MessagePole")

    def _add_message(self, type: str, text: str, username: str = None):
        new_message = MessageItem(text, username)
        new_message.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)

        if type == "my":
            new_message.WidgetContent.setObjectName("myMessage")

            self.MessageAreaContentLayout.addWidget(QLabel())
            self.MessageAreaContentLayout.addWidget(QLabel())
            self.MessageAreaContentLayout.addWidget(new_message)

        elif type == "other_user":
            new_message.WidgetContent.setObjectName("otherUserMessage")

            self.MessageAreaContentLayout.addWidget(new_message)
            self.MessageAreaContentLayout.addWidget(QLabel())
            self.MessageAreaContentLayout.addWidget(QLabel())

        elif type == "special":
            new_message.WidgetContent.setObjectName("specialMessage")

            self.MessageAreaContentLayout.addWidget(QLabel())
            self.MessageAreaContentLayout.addWidget(new_message)
            self.MessageAreaContentLayout.addWidget(QLabel())

        else:
            return False

        logger.info(f"add new message type: {type} text: {text}")

        return new_message
