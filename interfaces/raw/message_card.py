# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'message_card.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MessageCard(object):
    def setupUi(self, MessageCard):
        if not MessageCard.objectName():
            MessageCard.setObjectName(u"MessageCard")
        MessageCard.resize(94, 50)
        self.verticalLayout = QVBoxLayout(MessageCard)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.WidgetContent = QWidget(MessageCard)
        self.WidgetContent.setObjectName(u"WidgetContent")
        self.vboxLayout = QVBoxLayout(self.WidgetContent)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.usernameLabel = QLabel(self.WidgetContent)
        self.usernameLabel.setObjectName(u"usernameLabel")

        self.vboxLayout.addWidget(self.usernameLabel)

        self.textLabel = QLabel(self.WidgetContent)
        self.textLabel.setObjectName(u"textLabel")

        self.vboxLayout.addWidget(self.textLabel)


        self.verticalLayout.addWidget(self.WidgetContent)


        self.retranslateUi(MessageCard)

        QMetaObject.connectSlotsByName(MessageCard)
    # setupUi

    def retranslateUi(self, MessageCard):
        MessageCard.setWindowTitle(QCoreApplication.translate("MessageCard", u"Form", None))
        self.usernameLabel.setText(QCoreApplication.translate("MessageCard", u"TextLabel", None))
        self.textLabel.setText(QCoreApplication.translate("MessageCard", u"TextLabel", None))
    # retranslateUi

