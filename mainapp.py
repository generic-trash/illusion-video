from flask import Flask, request, redirect
from flask_sockets import Sockets
from geventwebsocket.handler import WebSocketHandler
from os import environ
from gevent.pywsgi import WSGIServer
from incrementor import Noob
uid = Noob()
app = Flask(__name__)
websocket = Sockets(app)


@websocket.route('/echo')
def echo(ws):
    user = int(request.cookies.get('id'))
    while True:
        msg = ws.receive()
        if msg:
            with open('temp_user_0', 'ab+') as t0, open('temp_user_1', 'ab+') as t1:
                if user == 0:
                    t0.seek(0)
                    t0.write(msg)
                    ws.send(t1.read())
                elif user == 1:
                    t1.seek(0)
                    t1.write(msg)
                    ws.send(t0.read())


@app.route('/')
def hi():
    resp = redirect("/static/Recording.html")
    resp.set_cookie('id', str(uid.val))
    uid.increment()
    return resp


if __name__ == '__main__':
    http_server = WSGIServer(('', int(environ.get('PORT'))), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
