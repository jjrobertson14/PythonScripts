#!/usr/bin/python3.5

import asyncio
import datetime
import random
import websockets
import logging
logger = logging.getLogger('websockets')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

#@asyncio.coroutine
async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

#async def handler(websocket, path):
#    while True:
#        message = await websocket.recv()
#        print(message)
#        await consumer(message)

#connected = set()
#
#async def handler(websocket, path):
#    global connected
#    # Register.
#    connected.add(websocket)
#    try:
#        # Implement logic here.
#        await asyncio.wait([ws.send("Hello!") for ws in connected])
#        await asyncio.sleep(10)
#    finally:
#        # Unregister.
#        connected.remove(websocket)


start_server = websockets.serve(time, '127.0.0.1', 50000)

print ('anything')
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
