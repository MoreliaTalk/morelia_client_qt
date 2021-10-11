import unittest
import websockets.server
from modules.server_connection.server_com import ServerCom


class TestConnectToServer(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.server_com = ServerCom()

    async def test_normal_connect(self):
        async def server_method(websocket, path):
            print(websocket, path)

        async with websockets.server.serve(server_method, "localhost", 8765):
            self.assertIsNone(await self.server_com.connect_to_server("ws://localhost:8765"))

    async def test_not_existent_address_connect(self):
        with self.assertRaises(ConnectionRefusedError):
            self.assertIsNone(await self.server_com.connect_to_server("ws://localhost:8765"))

if __name__ == "__main__":
    unittest.main()
