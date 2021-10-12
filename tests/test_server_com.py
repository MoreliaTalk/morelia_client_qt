import unittest
import websockets.server
from modules.server_connection.server_com import ServerCom


class TestConnectAndDisconnect(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.server_com = ServerCom()

    async def test_normal_connect(self):
        async def server_method(websocket, path):
            pass

        async with websockets.server.serve(server_method, "localhost", 8765):
            self.assertIsNone(await self.server_com.connect_to_server("ws://localhost:8765"))

    async def test_not_existent_address_connect(self):
        with self.assertRaises(ConnectionRefusedError):
            self.assertIsNone(await self.server_com.connect_to_server("ws://localhost:8766"))

    async def test_disconnect(self):
        async def server_method(websocket, path):
            pass

        async with websockets.server.serve(server_method, "localhost", 8767):
            await self.server_com.connect_to_server("ws://localhost:8767")
            self.assertIsNone(await self.server_com.disconnect_from_server())


if __name__ == "__main__":
    unittest.main()
