#!/usr/bin/env python
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder='./')
app.config['SECRET_KEY'] = 'secret!'
db = []
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('client_Updata')
def client_msg(msg):
    print("0")
    db.append([123, 12324421, 24])
    emit('server_response', {'data': [123, 12324421, 24]})


@socketio.on('client_event')
def client_msg(msg):
    print(msg['data'])
    db.append(msg['data'])
    emit('server_response', {'data': msg['data']})


@socketio.on('connect_event')
def connected_msg(msg):
    print("socketio連接成功")
    for i in db:
        emit('server_response', {'data': i})


if __name__ == '__main__':
    try:
        socketio.run(app, host='0.0.0.0')
    except:
        print("退出")