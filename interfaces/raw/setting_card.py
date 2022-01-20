# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting_card.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_SettingCard(object):
    def setupUi(self, SettingCard):
        if not SettingCard.objectName():
            SettingCard.setObjectName(u"SettingCard")
        SettingCard.resize(94, 38)
        self.horizontalLayout = QHBoxLayout(SettingCard)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(SettingCard)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.retranslateUi(SettingCard)

        QMetaObject.connectSlotsByName(SettingCard)
    # setupUi

    def retranslateUi(self, SettingCard):
        SettingCard.setWindowTitle(QCoreApplication.translate("SettingCard", u"Form", None))
        self.label.setText(QCoreApplication.translate("SettingCard", u"TextLabel", None))
    # retranslateUi

