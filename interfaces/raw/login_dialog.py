# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_loginDialog(object):
    def setupUi(self, loginDialog):
        if not loginDialog.objectName():
            loginDialog.setObjectName(u"loginDialog")
        loginDialog.setWindowModality(Qt.ApplicationModal)
        loginDialog.resize(383, 205)
        loginDialog.setWindowOpacity(1.000000000000000)
        self.verticalLayout = QVBoxLayout(loginDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.loginTabWidget = QTabWidget(loginDialog)
        self.loginTabWidget.setObjectName(u"loginTabWidget")
        self.loginTabWidget.setMinimumSize(QSize(365, 0))
        self.loginTabWidget.setMaximumSize(QSize(16777215, 234))
        self.signInTab = QWidget()
        self.signInTab.setObjectName(u"signInTab")
        self.verticalLayout_2 = QVBoxLayout(self.signInTab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formSignInLayout = QFormLayout()
        self.formSignInLayout.setObjectName(u"formSignInLayout")
        self.formSignInLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.formSignInLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.loginLabel = QLabel(self.signInTab)
        self.loginLabel.setObjectName(u"loginLabel")

        self.formSignInLayout.setWidget(0, QFormLayout.LabelRole, self.loginLabel)

        self.loginLineEdit = QLineEdit(self.signInTab)
        self.loginLineEdit.setObjectName(u"loginLineEdit")

        self.formSignInLayout.setWidget(0, QFormLayout.FieldRole, self.loginLineEdit)

        self.passwordLabel = QLabel(self.signInTab)
        self.passwordLabel.setObjectName(u"passwordLabel")

        self.formSignInLayout.setWidget(1, QFormLayout.LabelRole, self.passwordLabel)

        self.passwordLineEdit = QLineEdit(self.signInTab)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.formSignInLayout.setWidget(1, QFormLayout.FieldRole, self.passwordLineEdit)


        self.verticalLayout_2.addLayout(self.formSignInLayout)

        self.loginTabWidget.addTab(self.signInTab, "")
        self.registerTab = QWidget()
        self.registerTab.setObjectName(u"registerTab")
        self.verticalLayout_3 = QVBoxLayout(self.registerTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formRegisterLayout = QFormLayout()
        self.formRegisterLayout.setObjectName(u"formRegisterLayout")
        self.formRegisterLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.loginNameLabel = QLabel(self.registerTab)
        self.loginNameLabel.setObjectName(u"loginNameLabel")

        self.formRegisterLayout.setWidget(0, QFormLayout.LabelRole, self.loginNameLabel)

        self.loginNameLineEdit = QLineEdit(self.registerTab)
        self.loginNameLineEdit.setObjectName(u"loginNameLineEdit")

        self.formRegisterLayout.setWidget(0, QFormLayout.FieldRole, self.loginNameLineEdit)

        self.passwordRegisterLabel = QLabel(self.registerTab)
        self.passwordRegisterLabel.setObjectName(u"passwordRegisterLabel")

        self.formRegisterLayout.setWidget(1, QFormLayout.LabelRole, self.passwordRegisterLabel)

        self.passwordRegisterLineEdit = QLineEdit(self.registerTab)
        self.passwordRegisterLineEdit.setObjectName(u"passwordRegisterLineEdit")
        self.passwordRegisterLineEdit.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.passwordRegisterLineEdit.setEchoMode(QLineEdit.Password)

        self.formRegisterLayout.setWidget(1, QFormLayout.FieldRole, self.passwordRegisterLineEdit)

        self.displayNameLabel = QLabel(self.registerTab)
        self.displayNameLabel.setObjectName(u"displayNameLabel")

        self.formRegisterLayout.setWidget(2, QFormLayout.LabelRole, self.displayNameLabel)

        self.displayNameLineEdit = QLineEdit(self.registerTab)
        self.displayNameLineEdit.setObjectName(u"displayNameLineEdit")

        self.formRegisterLayout.setWidget(2, QFormLayout.FieldRole, self.displayNameLineEdit)

        self.eMailLabel = QLabel(self.registerTab)
        self.eMailLabel.setObjectName(u"eMailLabel")

        self.formRegisterLayout.setWidget(3, QFormLayout.LabelRole, self.eMailLabel)

        self.eMailLineEdit = QLineEdit(self.registerTab)
        self.eMailLineEdit.setObjectName(u"eMailLineEdit")
        self.eMailLineEdit.setInputMethodHints(Qt.ImhEmailCharactersOnly)

        self.formRegisterLayout.setWidget(3, QFormLayout.FieldRole, self.eMailLineEdit)


        self.verticalLayout_3.addLayout(self.formRegisterLayout)

        self.loginTabWidget.addTab(self.registerTab, "")

        self.verticalLayout.addWidget(self.loginTabWidget)

        self.bottomHorizontalLayout = QHBoxLayout()
        self.bottomHorizontalLayout.setObjectName(u"bottomHorizontalLayout")
        self.settingsPushButton = QPushButton(loginDialog)
        self.settingsPushButton.setObjectName(u"settingsPushButton")

        self.bottomHorizontalLayout.addWidget(self.settingsPushButton)

        self.bottomHorizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bottomHorizontalLayout.addItem(self.bottomHorizontalSpacer)

        self.okPushButton = QPushButton(loginDialog)
        self.okPushButton.setObjectName(u"okPushButton")

        self.bottomHorizontalLayout.addWidget(self.okPushButton)

        self.cancelPushButton = QPushButton(loginDialog)
        self.cancelPushButton.setObjectName(u"cancelPushButton")

        self.bottomHorizontalLayout.addWidget(self.cancelPushButton)


        self.verticalLayout.addLayout(self.bottomHorizontalLayout)


        self.retranslateUi(loginDialog)

        self.loginTabWidget.setCurrentIndex(0)
        self.okPushButton.setDefault(True)


        QMetaObject.connectSlotsByName(loginDialog)
    # setupUi

    def retranslateUi(self, loginDialog):
        loginDialog.setWindowTitle(QCoreApplication.translate("loginDialog", u"Authentification", None))
        self.loginLabel.setText(QCoreApplication.translate("loginDialog", u"Login name", None))
        self.passwordLabel.setText(QCoreApplication.translate("loginDialog", u"Password", None))
        self.loginTabWidget.setTabText(self.loginTabWidget.indexOf(self.signInTab), QCoreApplication.translate("loginDialog", u"Sign in", None))
        self.loginNameLabel.setText(QCoreApplication.translate("loginDialog", u"Login name", None))
        self.passwordRegisterLabel.setText(QCoreApplication.translate("loginDialog", u"Password", None))
        self.displayNameLabel.setText(QCoreApplication.translate("loginDialog", u"Display name", None))
        self.eMailLabel.setText(QCoreApplication.translate("loginDialog", u"E-Mail", None))
        self.loginTabWidget.setTabText(self.loginTabWidget.indexOf(self.registerTab), QCoreApplication.translate("loginDialog", u"Register", None))
        self.settingsPushButton.setText(QCoreApplication.translate("loginDialog", u"\u2699", None))
        self.okPushButton.setText(QCoreApplication.translate("loginDialog", u"OK", None))
        self.cancelPushButton.setText(QCoreApplication.translate("loginDialog", u"Cancel", None))
    # retranslateUi

