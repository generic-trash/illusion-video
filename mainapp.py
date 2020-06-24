from quart import Quart, request, send_file, websocket as ws
import asyncio
from functools import wraps
from incrementor import Noob, Blob

video_evts = asyncio.Event()
audio_evts = asyncio.Event()
uid = Noob()
t0 = Blob()
t1 = Blob()
t2 = Blob()
t3 = Blob()
app = Quart(__name__)


@app.websocket('/echo')
async def echo():
    wshash = 0
    dt = t1.get_data()
    if dt:
        await ws.send(dt)
    while True:
        await video_evts.wait()
        if wshash != hash(t0):
            await ws.send(t0.get_data())
            wshash = hash(t0)


@app.websocket('/audio')
async def audio():
    wshash = 0
    dt = t3.get_data()
    if dt:
        await ws.send(dt)
    while True:
        await audio_evts.wait()
        if wshash != hash(t2):
            await ws.send(t2.get_data())
            wshash = hash(t2)


@app.route('/')
async def hi():
    return await send_file("static/Recording.html")


@app.websocket('/streampoint')
async def streampoint():
    wshash = 0
    while True:
        msg = await ws.receive()
        if msg:
            t0.set_data(msg)
            if wshash == 0:
                t1.set_data(msg)
                wshash = hash(t1)
            video_evts.set()


@app.websocket('/audiostream')
async def astreampoint():
    wshash = 0
    while True:
        msg = await ws.receive()
        if msg:
            t2.set_data(msg)
            if wshash == 0:
                t3.set_data(msg)
                wshash = hash(t3)
            audio_evts.set()


@app.route('/')
async def viewer_url():
    return await send_file('static/Recording.html')


@app.route('/stream')
async def streamer_url():
    return await send_file('static/Streaming.html')


if __name__ == '__main__':
    app.run()
