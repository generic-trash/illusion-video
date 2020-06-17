from flask import Flask, request, send_file
from flask_sockets import Sockets
from geventwebsocket.handler import WebSocketHandler
from os import environ
from gevent.pywsgi import WSGIServer
from incrementor import Noob, Blob

uid = Noob()
t0 = Blob()
t1 = Blob()
t2 = Blob()
t3 = Blob()
app = Flask(__name__)
websocket = Sockets(app)


@websocket.route('/echo')
def echo(ws):
    wshash = 0
    dt = t1.get_data()
    if dt:
        ws.send(dt)
    while True:
        msg = ws.receive()
        if wshash != hash(t0):
            ws.send(t0.get_data())
            wshash = hash(t0)


@websocket.route('/audio')
def audio(ws):
    wshash = 0
    dt = t3.get_data()
    if dt:
        ws.send(dt)
    while True:
        msg = ws.receive()
        if wshash != hash(t2):
            ws.send(t2.get_data())
            wshash = hash(t2)


@app.route('/')
def hi():
    return send_file("static/Recording.html")


@websocket.route('/streampoint')
def streampoint(ws):
    wshash = 0
    while True:
        msg = ws.receive()
        if msg:
            t0.set_data(msg)
            if wshash == 0:
                t1.set_data(msg)
                wshash = hash(t1)


@websocket.route('/audiostream')
def streampoint(ws):
    wshash = 0
    while True:
        msg = ws.receive()
        if msg:
            t2.set_data(msg)
            if wshash == 0:
                t3.set_data(msg)
                wshash = hash(t3)


@app.route('/stream')
def stream():
    return send_file('static/Streaming.html')


@app.route('/')
def viewer_url():
    return send_file('static/Recording.html')


@app.route('/stream')
def streamer_url():
    return send_file('static/Streaming.html')


if __name__ == '__main__':
    http_server = WSGIServer(('', int(environ.get('PORT'))), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
