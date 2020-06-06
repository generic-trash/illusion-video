from flask import Flask
from flask_uwsgi_websocket import GeventWebSocket

app = Flask(__name__)
websocket = GeventWebSocket(app)


@websocket.route('/echo')
def echo(ws):
    while True:
        msg = ws.receive()
        ws.send(msg)


if __name__ == '__main__':
    app.run(gevent=100, port=10000)
