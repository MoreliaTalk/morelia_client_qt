from datetime import datetime


import requests
from PyQt5 import QtWidgets, QtCore
import clientui
import user_and_passui
import errorui

url = 'http://127.0.0.1:5000/'
version = "1.0.0"

class Error_window(QtWidgets.QMainWindow, errorui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.pressed.connect(self.close)
        

class UserPass(QtWidgets.QMainWindow, user_and_passui.Ui_MainWindow):
    def __init__(self, url, version):
        super().__init__()
        self.setupUi(self)
        self.url = url
        self.version = version

        self.lineEdit_2.setEchoMode(self.lineEdit_2.Password)
        self.pushButton.pressed.connect(self.passworder)
        self.pushButton.pressed.connect(self.controler)

        users = requests.get(
            self.url + '/users',
            json={'pass': 'hellomyfriend@12345'})

        self.users = users.json()['users']
        self.label_4.setText(f'v {self.version}')

    def passworder(self):
        return {'username': self.lineEdit.text(), 
                'password': self.lineEdit_2.text()}

    def controler(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if username.strip() == '':
            self.lineEdit.setStyleSheet("background: rgb(255, 74, 74); ")
            self.lineEdit.setText('')
        else:
            self.lineEdit.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:0.852, y2:0.863636, stop:0 rgba(179, 255, 254, 255), stop:1 rgba(255, 216, 246, 255));")
        if password.strip() == '':
            self.lineEdit_2.setStyleSheet("background: rgb(255, 74, 74); ")
            self.lineEdit_2.setText('')
        else:
            self.lineEdit_2.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:0.852, y2:0.863636, stop:0 rgba(179, 255, 254, 255), stop:1 rgba(255, 216, 246, 255));")
        if username.strip() != '' and password.strip() != '':
            if username in self.users.keys():
                if self.users[username] == password:
                    self.close()
                else:
                    self.lineEdit_2.setStyleSheet("background: rgb(255, 74, 74); ")
            else:
                requests.get(
                self.url + '/add_user',
                json={'username' : username, 
                'password' : password})
                self.close()


class Client_messenger(QtWidgets.QMainWindow, clientui.Ui_MainWindow):
    def __init__(self, url, username, password, version):
        super().__init__()
        self.setupUi(self)

        self.url = url
        self.username = username
        self.password = password
        self.version = version
        self.dark = 0

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
        self.label.setStyleSheet("color: rgb(255, 255, 255); background-color:  rgba(0, 255, 254, 0);")
        self.label_2.setStyleSheet("color: rgb(255, 255, 255); background-color:  rgba(0, 255, 254, 0);")
        self.centralwidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.238636, stop:0 rgba(2, 0, 191, 255), stop:1 rgba(0, 2, 97, 255));")
        self.checkBox.setStyleSheet("color: rgb(255, 255, 255); background-color:  rgba(0, 255, 254, 0);")
        self.textBrowser.setStyleSheet("color: rgb(255, 255, 255); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.238636, stop:0 rgba(2, 0, 191, 255), stop:1 rgba(0, 2, 97, 255));")
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.238636, stop:0 rgba(2, 0, 191, 255), stop:1 rgba(0, 2, 97, 255));")
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.238636, stop:0 rgba(2, 0, 191, 255), stop:1 rgba(0, 2, 97, 255));")

    def not_dark_theme(self):
        self.label.setStyleSheet("color: rgb(0, 0, 0); background-color:  rgba(0, 255, 254, 0);")
        self.label_2.setStyleSheet("color: rgb(0, 0, 0); background-color:  rgba(0, 255, 254, 0);")
        self.checkBox.setStyleSheet("color: rgb(0, 0, 0); background-color:  rgba(0, 255, 254, 0);")
        self.textBrowser.setStyleSheet("color: rgb(0, 0, 0); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.852, y2:0.863636, stop:0 rgba(179, 255, 254, 255), stop:1 rgba(255, 216, 246, 255));")
        self.textEdit.setStyleSheet("color: rgb(0, 0, 0); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.852, y2:0.863636, stop:0 rgba(179, 255, 254, 255), stop:1 rgba(255, 216, 246, 255));")
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0); background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.852, y2:0.863636, stop:0 rgba(179, 255, 254, 255), stop:1 rgba(255, 216, 246, 255));")
        self.centralwidget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.852, y2:0.863636, stop:0 rgba(179, 255, 254, 255), stop:1 rgba(255, 216, 246, 255));")

    def theme(self):
        if self.dark == 0:
            self.dark_theme()
            self.dark = 1
        else:
            self.not_dark_theme()
            self.dark = 0

try:
    requests.get(url)
    app = QtWidgets.QApplication([])
    window_pass = UserPass(url, version)
    window_pass.show()
    app.exec_()
    user = window_pass.passworder()
    users = requests.get(
                url + '/users',
                json={'pass': 'hellomyfriend@12345'})
    users = users.json()['users']
    if user['username'] in users.keys():
        if user['password'] == users[user['username']]:
            window = Client_messenger(url, user['username'], user['password'], version)
            window.show()
            app.exec_()
except:
    app = QtWidgets.QApplication([])
    window_error = Error_window()
    window_error.show()
    app.exec_()