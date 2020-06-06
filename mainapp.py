from flask import Flask
from flask_sockets import Sockets
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer

app = Flask(__name__)
websocket = Sockets(app)


@websocket.route('/echo')
def echo(ws):
    while True:
        msg = ws.receive()
        ws.send(msg)


@app.route('/')
def hi():
    return "Hello world"


if __name__ == '__main__':
    http_server = WSGIServer(('', 10000), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
