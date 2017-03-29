#/usr/bin/python3.5

import random
import asyncio
import websockets

async def test(websocket, path):
    while True:
        message = 'hello'
        await websocket.send(message)
        await asyncio.sleep(random.random() * 3)

start_client = websockets.connect(test, '10.0.0.3', 50000)

asyncio.get_event_loop().run_until_complete(start_client)
asyncio.get_event_loop().run_forever()
