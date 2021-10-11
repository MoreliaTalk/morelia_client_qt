import websockets
# import asyncio

class ServerCom:
    def __init__(self):
        pass

    async def connect_to_server(self, url: str):
        self.ws = await websockets.connect(url)

    async def disconnect_from_server(self):
        await self.ws.close()

"""async def main():
    a = ServerCom()
    await a.connect_to_server("ws://localhost:8000/ws")
    await a.disconnect_from_server()

asyncio.run(main())"""