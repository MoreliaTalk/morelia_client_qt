import time
from datetime import datetime

from flask import Flask, request

app = Flask(__name__)
server_start = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
messages = []
users = {
    'bot': 'bot_password'
}

@app.route("/")
def hello():
    return 'Hello, User! <a href="/status">status</a>'


@app.route("/status")
def status():
    return {
        'status': True,
        'name': 'vika_kiroy_messenger',
        'time': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
        'users_count': len(users),
        'messages_count': len(messages)
    }


@app.route("/send_message")
def send_message():
    username = request.json['username']
    text = request.json['text']

    messages.append({'username': username, 'text': text, 'timestamp': time.time()})
    return {'ok': True}


@app.route("/get_messages")
def get_messages():
    after = float(request.args['after'])

    result = []

    for message in messages:
        if message['timestamp'] > after:
            result.append(message)
    return {
        'messages': result
    }

@app.route("/add_user")
def add_user():
    users[request.json['username']] = request.json['password']

@app.route("/users")    
def userser():
    return {'users': users}

app.run(debug=True)