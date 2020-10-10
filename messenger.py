from datetime import datetime

import requests
from PyQt5 import QtWidgets, QtCore
import clientui
import user_and_passui
import errorui

URL = 'http://127.0.0.1:5000/'
VERSION = "1.0.0"
THEMES = ["color: rgb(255, 255, 255); background-color:  rgba(0, 255, 254, 0);", 
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.238636, stop:0 rgba(2, 0, 191, 255), stop:1 rgba(0, 2, 97, 255));", 
        "color: rgb(0, 0, 0); background-color:  rgba(0, 255, 254, 0);",
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(187, 220, 255, 255), stop:1 rgba(150, 228, 240, 255));",
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(187, 220, 255, 255), stop:1 rgba(150, 228, 240, 255));",
        "background: rgb(255, 74, 74);"
        ]


class Error_window(QtWidgets.QMainWindow, errorui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(self.close)
        

class UserPass(QtWidgets.QMainWindow, user_and_passui.Ui_Messenger):
    def __init__(self, url, version, light_theme, error_theme):
        super().__init__()
        self.setupUi(self)
        self.url = URL
        self.version = VERSION

        self.light_theme = light_theme
        self.error_theme = error_theme

        self.lineEdit_password.setEchoMode(self.lineEdit_password.Password)
        self.pushButton.pressed.connect(self.passworder)
        self.pushButton.pressed.connect(self.controler)

        users = requests.get(
            self.url + '/users',
            json={'pass': 'hellomyfriend@12345'})

        self.users = users.json()['users']
        self.label_version.setText(f'v {self.version}')

    def passworder(self):
        return {'username': self.lineEdit_user.text(), 
                'password': self.lineEdit_password.text()}

    def controler(self):
        username = self.lineEdit_user.text()
        password = self.lineEdit_password.text()
        if username.strip() == '':
            self.lineEdit_user.setStyleSheet(self.light_theme)
            self.lineEdit_user.setText('')
        else:
            self.lineEdit_user.setStyleSheet(self.error_theme)
        if password.strip() == '':
            self.lineEdit_password.setStyleSheet(self.light_theme)
            self.lineEdit_password.setText('')
        else:
            self.lineEdit_password.setStyleSheet(self.error_theme)
        if username.strip() != '' and password.strip() != '':
            if username in self.users.keys():
                if self.users[username] == password:
                    self.close()
                else:
                    self.lineEdit_password.setStyleSheet(self.light_theme)
            else:
                requests.get(
                self.url + '/add_user',
                json={'username' : username, 
                'password' : password})
                self.close()


class Client_messenger(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
    def __init__(self, url, username, password, version, light_theme_1, light_theme_2, dark_theme_1, dark_theme_2):
        super().__init__()
        self.setupUi(self)

        self.url = URL
        self.username = username
        self.password = password
        self.version = VERSION
        self.dark = 0

        self.dark_theme_1 = dark_theme_1
        self.dark_theme_2 = dark_theme_2
        self.light_theme_1 = light_theme_1
        self.light_theme_2 = light_theme_2


        self.label_2.setText(f'v {self.version}')

        self.pushButton.pressed.connect(self.send_message)

        self.checkBox.stateChanged.connect(self.theme)

        self.last_timestamp = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_messages)
        self.timer.start(1000)


    def send_message(self):
        text = self.textEdit.toPlainText()

        requests.get(
            self.url + '/send_message',
            json={
                'username': self.username,
                'text': text
            }
        )

        self.textEdit.setText('')
        self.textEdit.repaint()
        self.textEdit.setFocus()

    def update_messages(self):
        response = requests.get(
            self.url + '/get_messages',
            params={'after': self.last_timestamp}
        )
        messages = response.json()['messages']

        for message in messages:
            if message['text'].strip() != '':
                dt = datetime.fromtimestamp(message['timestamp'])
                dt = dt.strftime('%d/%m/%Y %H:%M:%S')
                self.textBrowser.append(dt + ' ' + message['username'])
                self.textBrowser.append(message['text'].strip())
                self.textBrowser.append('')
            self.last_timestamp = message['timestamp']

    def dark_theme(self):
        self.label.setStyleSheet(self.dark_theme_1)
        self.label_2.setStyleSheet(self.dark_theme_1)
        self.centralwidget.setStyleSheet(self.dark_theme_2)
        self.checkBox.setStyleSheet(self.dark_theme_1)
        self.textBrowser.setStyleSheet(self.dark_theme_2)
        self.textEdit.setStyleSheet(self.dark_theme_2)
        self.pushButton.setStyleSheet(self.dark_theme_2)

    def not_dark_theme(self):
        self.label.setStyleSheet(self.light_theme_1)
        self.label_2.setStyleSheet(self.light_theme_1)
        self.checkBox.setStyleSheet(self.light_theme_1)
        self.textBrowser.setStyleSheet(self.light_theme_2)
        self.textEdit.setStyleSheet(self.light_theme_2)
        self.pushButton.setStyleSheet(self.light_theme_2)
        self.centralwidget.setStyleSheet(self.light_theme_2)

    def theme(self):
        if self.dark == 0:
            self.dark_theme()
            self.dark = 1
        else:
            self.not_dark_theme()
            self.dark = 0

if str(requests.get(URL)) == '<Response [200]>':
    app = QtWidgets.QApplication([])
    window_pass = UserPass(URL, 
        VERSION, 
        THEMES[5], 
        THEMES[4])
    window_pass.show()
    app.exec_()
    user = window_pass.passworder()
    users = requests.get(
                URL + '/users',
                json={'pass': 'hellomyfriend@12345'})
    users = users.json()['users']
    if user['username'] in users.keys():
        if user['password'] == users[user['username']]:
            window = Client_messenger(URL, 
                user['username'], 
                user['password'], 
                VERSION, 
                THEMES[2], 
                THEMES[3], 
                THEMES[0], 
                THEMES[1])
            window.show()
            app.exec_()
else:
    app = QtWidgets.QApplication([])
    window_error = Error_window()
    window_error.show()
    app.exec_()