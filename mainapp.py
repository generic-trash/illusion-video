from flask import Flask, send_file
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

@app.route('/')
def viewer_url():
    return send_file('static/Recording.html')

@app.route('/stream')
def viewer_url():
    return send_file('static/Streaming.html')


if __name__ == '__main__':
    socketio.run(app, port=environ.get('PORT'))
