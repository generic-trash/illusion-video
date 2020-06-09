from flask import Flask, request, send_file
from flask_sockets import Sockets
from geventwebsocket.handler import WebSocketHandler
from os import environ
from gevent.pywsgi import WSGIServer
from incrementor import Noob, Blob

uid = Noob()
t0 = Blob()
t1 = Blob()
app = Flask(__name__)
websocket = Sockets(app)


@websocket.route('/echo')
def echo(ws):
    wshash = 0
    while True:
        msg = ws.receive()
        if wshash != hash(t0):
            ws.send(t0.get_data())
            wshash = hash(t0)


@app.route('/')
def hi():
    return send_file("static/Recording.html")

@app.route('/stream')
def stream():
    return send_file('static/Streaming.html')

if __name__ == '__main__':
    http_server = WSGIServer(('', int(environ.get('PORT'))), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
