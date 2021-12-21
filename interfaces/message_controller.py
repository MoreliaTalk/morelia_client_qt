from PySide6.QtWidgets import QGridLayout, QLabel, QSizePolicy, QWidget
from loguru import logger

from interfaces.chats_controller import ChatsController
from modules.database.clientdb import ClientDb
from interfaces.raw.message_card import Ui_MessageCard


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
    def __init__(self,
                 db: ClientDb,
                 chats_controller: ChatsController,
                 message_area_content_layout: QGridLayout):
        super().__init__()

        self.message_area_content_layout: QGridLayout = message_area_content_layout

        for i in range(3):
            self.message_area_content_layout.setColumnStretch(i, 1)

        self.db = db
        self.chats_controller = chats_controller

    def load_messages_current_chat(self, chat_uuid: str):
        self._clear()

        for chat in self.chats_controller.list_chats:
            if chat.uuid == chat_uuid:
                chat.setStyleSheet("background-color: #424242")
            else:
                chat.setStyleSheet("")

        messages_tuple = list(self.db.list_messages(flow_uuid=chat_uuid))
        messages_tuple.reverse()

        if len(messages_tuple):
            for message in messages_tuple:
                if message.user_uuid == self.db.get_param("user_uuid"):
                    self._add_message("my", message.text)
                else:
                    if self.db.get_flow(flow_uuid=chat_uuid).flowType == "group":
                        self._add_message("other_user", message.text, message.username)
                    else:
                        self._add_message("other_user", message.text)

        else:
            self._add_message("special", "Здесь пока нет сообщений")

    def _clear(self):
        messages = self.message_area_content_layout.parentWidget().findChildren(MessageItem)
        for mes in messages:
            mes.deleteLater()

        logger.info("clear MessagePole")

    def _add_message(self, mes_type: str, mes_text: str, username: str = None):
        new_message = MessageItem(mes_text, username)
        new_message.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)

        if mes_type == "my":
            new_message.WidgetContent.setObjectName("myMessage")

            self.message_area_content_layout.addWidget(QLabel())
            self.message_area_content_layout.addWidget(QLabel())
            self.message_area_content_layout.addWidget(new_message)

        elif mes_type == "other_user":
            new_message.WidgetContent.setObjectName("otherUserMessage")

            self.message_area_content_layout.addWidget(new_message)
            self.message_area_content_layout.addWidget(QLabel())
            self.message_area_content_layout.addWidget(QLabel())

        elif mes_type == "special":
            new_message.WidgetContent.setObjectName("specialMessage")

            self.message_area_content_layout.addWidget(QLabel())
            self.message_area_content_layout.addWidget(new_message)
            self.message_area_content_layout.addWidget(QLabel())

        else:
            return False

        logger.info(f"add new message type: {mes_type} text: {mes_text}")

        return new_message
