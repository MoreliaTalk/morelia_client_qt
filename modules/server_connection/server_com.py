import websockets.client
from loguru import logger


class ServerCom:
    def __init__(self, url: str):
        self.url = url
        self.connect()

    async def connect(self):
        self.ws = await websockets.client.connect(self.url)
        logger.info("Websocket connected to " + url)

    async def disconnect(self):
        await self.ws.wait_closed()
        logger.info("Websocket connection closed")

    async
