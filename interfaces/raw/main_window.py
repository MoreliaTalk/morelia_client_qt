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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLayout,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTextEdit, QToolButton,
    QVBoxLayout, QWidget)

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
        self.MessageArea = QScrollArea(self.centralwidget)
        self.MessageArea.setObjectName(u"MessageArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MessageArea.sizePolicy().hasHeightForWidth())
        self.MessageArea.setSizePolicy(sizePolicy1)
        self.MessageArea.setWidgetResizable(True)
        self.MessageAreaContent = QWidget()
        self.MessageAreaContent.setObjectName(u"MessageAreaContent")
        self.MessageAreaContent.setGeometry(QRect(0, 0, 628, 471))
        self.MessageAreaContentLayout = QGridLayout(self.MessageAreaContent)
        self.MessageAreaContentLayout.setObjectName(u"MessageAreaContentLayout")
        self.MessageAreaContentLayout.setHorizontalSpacing(0)
        self.MessageAreaContentLayout.setVerticalSpacing(3)
        self.MessageAreaContentLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.MessageAreaContentLayout.addItem(self.verticalSpacer, 0, 0, 1, 2)

        self.MessageArea.setWidget(self.MessageAreaContent)

        self.gridLayout.addWidget(self.MessageArea, 0, 1, 1, 1)

        self.InputArea = QHBoxLayout()
        self.InputArea.setSpacing(5)
        self.InputArea.setObjectName(u"InputArea")
        self.InputArea.setContentsMargins(0, 0, 0, 0)
        self.InputText = QTextEdit(self.centralwidget)
        self.InputText.setObjectName(u"InputText")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.InputText.sizePolicy().hasHeightForWidth())
        self.InputText.setSizePolicy(sizePolicy2)
        self.InputText.setMinimumSize(QSize(10, 10))

        self.InputArea.addWidget(self.InputText)

        self.SendButton = QPushButton(self.centralwidget)
        self.SendButton.setObjectName(u"SendButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.SendButton.sizePolicy().hasHeightForWidth())
        self.SendButton.setSizePolicy(sizePolicy3)
        self.SendButton.setMinimumSize(QSize(0, 0))

        self.InputArea.addWidget(self.SendButton)

        self.InputArea.setStretch(0, 5)
        self.InputArea.setStretch(1, 1)

        self.gridLayout.addLayout(self.InputArea, 1, 1, 1, 1)

        self.ChatList_And_SearchWidget = QWidget(self.centralwidget)
        self.ChatList_And_SearchWidget.setObjectName(u"ChatList_And_SearchWidget")
        self.verticalLayout = QVBoxLayout(self.ChatList_And_SearchWidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MenuAndSearchWidget = QWidget(self.ChatList_And_SearchWidget)
        self.MenuAndSearchWidget.setObjectName(u"MenuAndSearchWidget")
        self.Menu_and_Search_layout = QHBoxLayout(self.MenuAndSearchWidget)
        self.Menu_and_Search_layout.setSpacing(5)
        self.Menu_and_Search_layout.setObjectName(u"Menu_and_Search_layout")
        self.Menu_and_Search_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.Menu_and_Search_layout.setContentsMargins(5, 5, 5, 5)
        self.MenuButton = QToolButton(self.MenuAndSearchWidget)
        self.MenuButton.setObjectName(u"MenuButton")
        self.MenuButton.setMinimumSize(QSize(30, 30))

        self.Menu_and_Search_layout.addWidget(self.MenuButton)

        self.SearchLineEdit = QLineEdit(self.MenuAndSearchWidget)
        self.SearchLineEdit.setObjectName(u"SearchLineEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.SearchLineEdit.sizePolicy().hasHeightForWidth())
        self.SearchLineEdit.setSizePolicy(sizePolicy4)
        self.SearchLineEdit.setMinimumSize(QSize(0, 30))
        self.SearchLineEdit.setMaximumSize(QSize(16777215, 16777215))

        self.Menu_and_Search_layout.addWidget(self.SearchLineEdit)


        self.verticalLayout.addWidget(self.MenuAndSearchWidget)

        self.ChatListArea = QScrollArea(self.ChatList_And_SearchWidget)
        self.ChatListArea.setObjectName(u"ChatListArea")
        sizePolicy3.setHeightForWidth(self.ChatListArea.sizePolicy().hasHeightForWidth())
        self.ChatListArea.setSizePolicy(sizePolicy3)
        self.ChatListArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 313, 483))
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

        self.verticalLayout.addWidget(self.ChatListArea)

        self.verticalLayout.setStretch(1, 12)

        self.gridLayout.addWidget(self.ChatList_And_SearchWidget, 0, 0, 2, 1)

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
        self.MenuButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi

