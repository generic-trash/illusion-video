from flask import Flask, request, send_file
from flask_sockets import Sockets
from geventwebsocket.handler import WebSocketHandler
from os import environ
from gevent.pywsgi import WSGIServer
from incrementor import Noob, Blob

uid = Noob()
streamBlob = Blob()
app = Flask(__name__)
websocket = Sockets(app)


@websocket.route('/echo')
def echo(ws):
    isstreamer = int(request.cookies.get('id')) == 0
    wshash = 0
    while True:
        if isstreamer:
            msg = ws.receive()
            if msg:
                streamBlob.set_data(msg)
        elif wshash != hash(streamBlob):
            ws.send(streamBlob.get_data())
            wshash = hash(streamBlob)


@app.route('/')
def hi():
    resp = send_file("static/Recording.html")
    resp.set_cookie('id', str(uid.val))
    uid.increment()
    return resp


if __name__ == '__main__':
    http_server = WSGIServer(('', int(environ.get('PORT'))), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
