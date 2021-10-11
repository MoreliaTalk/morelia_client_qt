import websockets
from loguru import logger


class ServerCom:
    def __init__(self):
        pass

    async def connect_to_server(self, url: str):
        self.ws = await websockets.connect(url)
        logger.info("Websocket connected to "+url)

    async def disconnect_from_server(self):
        await self.ws.close()
        logger.info("Websocket connection closed")
