# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contact_card.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_ContactCard(object):
    def setupUi(self, ContactCard):
        if not ContactCard.objectName():
            ContactCard.setObjectName(u"ContactCard")
        ContactCard.resize(95, 40)
        ContactCard.setAutoFillBackground(True)
        self.gridLayout = QGridLayout(ContactCard)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.ContactCardContent = QWidget(ContactCard)
        self.ContactCardContent.setObjectName(u"ContactCardContent")
        self.ContactCardContentLayout = QHBoxLayout(self.ContactCardContent)
        self.ContactCardContentLayout.setObjectName(u"ContactCardContentLayout")
        self.ContactCardContentLayout.setContentsMargins(9, 9, 9, 9)
        self.ContactAvatar = QLabel(self.ContactCardContent)
        self.ContactAvatar.setObjectName(u"ContactAvatar")
        self.ContactAvatar.setMinimumSize(QSize(40, 40))
        self.ContactAvatar.setMaximumSize(QSize(40, 40))
        self.ContactAvatar.setAlignment(Qt.AlignCenter)

        self.ContactCardContentLayout.addWidget(self.ContactAvatar)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ChatNameLabel = QLabel(self.ContactCardContent)
        self.ChatNameLabel.setObjectName(u"ChatNameLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChatNameLabel.sizePolicy().hasHeightForWidth())
        self.ChatNameLabel.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.ChatNameLabel)

        self.ChatLastMessageLabel = QLabel(self.ContactCardContent)
        self.ChatLastMessageLabel.setObjectName(u"ChatLastMessageLabel")
        sizePolicy.setHeightForWidth(self.ChatLastMessageLabel.sizePolicy().hasHeightForWidth())
        self.ChatLastMessageLabel.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.ChatLastMessageLabel)


        self.ContactCardContentLayout.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.ContactCardContent, 0, 0, 1, 1)


        self.retranslateUi(ContactCard)

        QMetaObject.connectSlotsByName(ContactCard)
    # setupUi

    def retranslateUi(self, ContactCard):
        self.ContactAvatar.setText("")
        self.ChatNameLabel.setText(QCoreApplication.translate("ContactCard", u"TextLabel", None))
        self.ChatLastMessageLabel.setText(QCoreApplication.translate("ContactCard", u"TextLabel", None))
        pass
    # retranslateUi

