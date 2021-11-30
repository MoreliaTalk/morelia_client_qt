# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.InputArea = QHBoxLayout()
        self.InputArea.setSpacing(5)
        self.InputArea.setObjectName(u"InputArea")
        self.InputArea.setContentsMargins(0, 0, 0, 0)
        self.InputText = QTextEdit(self.centralwidget)
        self.InputText.setObjectName(u"InputText")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.InputText.sizePolicy().hasHeightForWidth())
        self.InputText.setSizePolicy(sizePolicy1)
        self.InputText.setMinimumSize(QSize(10, 10))

        self.InputArea.addWidget(self.InputText)

        self.SendButton = QPushButton(self.centralwidget)
        self.SendButton.setObjectName(u"SendButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.SendButton.sizePolicy().hasHeightForWidth())
        self.SendButton.setSizePolicy(sizePolicy2)
        self.SendButton.setMinimumSize(QSize(0, 0))

        self.InputArea.addWidget(self.SendButton)

        self.InputArea.setStretch(0, 5)
        self.InputArea.setStretch(1, 1)

        self.gridLayout.addLayout(self.InputArea, 1, 1, 1, 1)

        self.ChatListArea = QScrollArea(self.centralwidget)
        self.ChatListArea.setObjectName(u"ChatListArea")
        sizePolicy2.setHeightForWidth(self.ChatListArea.sizePolicy().hasHeightForWidth())
        self.ChatListArea.setSizePolicy(sizePolicy2)
        self.ChatListArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 313, 528))
        self.chatVerticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.chatVerticalLayout.setSpacing(0)
        self.chatVerticalLayout.setObjectName(u"chatVerticalLayout")
        self.chatVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ContactsContent = QVBoxLayout()
        self.ContactsContent.setObjectName(u"ContactsContent")

        self.chatVerticalLayout.addLayout(self.ContactsContent)

        self.chatVerticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.chatVerticalLayout.addItem(self.chatVerticalSpacer)

        self.ChatListArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.ChatListArea, 0, 0, 2, 1)

        self.MessageArea = QScrollArea(self.centralwidget)
        self.MessageArea.setObjectName(u"MessageArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.MessageArea.sizePolicy().hasHeightForWidth())
        self.MessageArea.setSizePolicy(sizePolicy3)
        self.MessageArea.setWidgetResizable(True)
        self.MessageAreaContent = QWidget()
        self.MessageAreaContent.setObjectName(u"MessageAreaContent")
        self.MessageAreaContent.setGeometry(QRect(0, 0, 628, 471))
        self.MessageAreaContentLayout = QGridLayout(self.MessageAreaContent)
        self.MessageAreaContentLayout.setSpacing(0)
        self.MessageAreaContentLayout.setObjectName(u"MessageAreaContentLayout")
        self.MessageAreaContentLayout.setContentsMargins(0, 5, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.MessageAreaContentLayout.addItem(self.verticalSpacer, 0, 0, 1, 2)

        self.MessageArea.setWidget(self.MessageAreaContent)

        self.gridLayout.addWidget(self.MessageArea, 0, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 9)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.SendButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

