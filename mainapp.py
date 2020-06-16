from flask import Flask, render_template
from os import environ
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yeetification'
socketio = SocketIO(app)


@socketio.on('streamvideo')
def message_handler(msg):
    emit('streamvid', msg, broadcast=True, include_self=False)


@socketio.on('streamaudio')
def message_handler(msg):
    emit('streamaud', msg, broadcast=True, include_self=False)


if __name__ == '__main__':
    socketio.run(app, port=environ.get('PORT'))
