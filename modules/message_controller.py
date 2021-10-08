from PyQt5.QtWidgets import QLabel, QSizePolicy


class MessageElement(QLabel):
    def __init__(self):
        super().__init__()


class MessageController:
    def __init__(self, MessageAreaContentLayout):
        super().__init__()

        self.MessageAreaContentLayout = MessageAreaContentLayout

    def add_message(self, type: str, text: str):
        new_message = MessageElement()
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

        return new_message
