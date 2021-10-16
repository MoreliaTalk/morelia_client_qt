# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/contact_card.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ContactCard(object):
    def setupUi(self, ContactCard):
        ContactCard.setObjectName("ContactCard")
        ContactCard.resize(95, 40)
        ContactCard.setAutoFillBackground(True)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ContactCard)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ContactAvatar = QtWidgets.QLabel(ContactCard)
        self.ContactAvatar.setMinimumSize(QtCore.QSize(40, 40))
        self.ContactAvatar.setMaximumSize(QtCore.QSize(40, 40))
        self.ContactAvatar.setText("")
        self.ContactAvatar.setAlignment(QtCore.Qt.AlignCenter)
        self.ContactAvatar.setObjectName("ContactAvatar")
        self.horizontalLayout.addWidget(self.ContactAvatar)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ChatNameLabel = QtWidgets.QLabel(ContactCard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChatNameLabel.sizePolicy().hasHeightForWidth())
        self.ChatNameLabel.setSizePolicy(sizePolicy)
        self.ChatNameLabel.setObjectName("ChatNameLabel")
        self.verticalLayout.addWidget(self.ChatNameLabel)
        self.ChatLastMessageLabel = QtWidgets.QLabel(ContactCard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ChatLastMessageLabel.sizePolicy().hasHeightForWidth())
        self.ChatLastMessageLabel.setSizePolicy(sizePolicy)
        self.ChatLastMessageLabel.setObjectName("ChatLastMessageLabel")
        self.verticalLayout.addWidget(self.ChatLastMessageLabel)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(ContactCard)
        QtCore.QMetaObject.connectSlotsByName(ContactCard)

    def retranslateUi(self, ContactCard):
        _translate = QtCore.QCoreApplication.translate
        self.ChatNameLabel.setText(_translate("ContactCard", "TextLabel"))
        self.ChatLastMessageLabel.setText(_translate("ContactCard", "TextLabel"))
