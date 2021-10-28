from PyQt5.QtWidgets import QLabel, QSizePolicy
from loguru import logger


class MessageController:
    def __init__(self, MessageAreaContentLayout):
        super().__init__()

        self.MessageAreaContentLayout = MessageAreaContentLayout

    def add_message(self, type: str, text: str):
        new_message = QLabel()
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
