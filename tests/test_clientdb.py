from unittest import TestCase

from modules.database import clientdb

import sqlite3


class TestClientDb(TestCase):
    @classmethod
    def setUpClass(cls):
        self.clientdb = clientdb.ClientDb("sqlite:/:memory:")
        pass

    def setUp(self):
        self.clientdb.create_db()
        self.clientdb.add_user("uuu1", "User1", "useremail1@server")
        self.clientdb.add_user("uuu2", "User2", "useremail2@server")
        self.clientdb.add_flow("fff1", "Chat1")
        self.clientdb.add_flow("fff2", "Chat2")
        self.clientdb.add_flow("fff3", "Chat3")
        self.clientdb.add_message("mmm1", "Message 1 in chat1 from user1", 10001,
                                  self.clientdb.get_user_id_by_uuid("uuu1"),
                                  self.clientdb.get_flow_id_by_uuid("fff1"))
        self.clientdb.add_message("mmm2", "Message 2 in chat1 from user2", 10002,
                                  self.clientdb.get_user_id_by_uuid("uuu2"),
                                  self.clientdb.get_flow_id_by_uuid("fff1"))
        self.clientdb.add_message("mmm3", "Message 3 in chat3 from user2", 10003,
                                  self.clientdb.get_user_id_by_uuid("uuu2"),
                                  self.clientdb.get_flow_id_by_uuid("fff3"))
        self.clientdb.set_param("ExistParam", "ExistParamValue")

    def tearDown(self):
        self.clientdb.delete_tables()

    def test_create_db(self):
        self.clientdb.delete_tables()
        self.clientdb.create_db()
        self.assertEqual(len(list(self.clientdb.list_messages(self.clientdb.get_flow_id_by_uuid("fff1")))), 0)
        self.assertEqual(len(list(self.clientdb.list_messages(self.clientdb.get_flow_id_by_uuid("fff3")))), 0)

    def test_delete_tables(self):
        self.clientdb.delete_tables()
        self.assertIsNone(self.clientdb.get_flow_id_by_uuid("fff1"))
        self.assertIsNone(self.clientdb.get_user_id_by_uuid("uuu1"))

    def test_add_user(self):
        self.assertIsNone(self.clientdb.get_user_id_by_uuid("uuu3"))
        self.clientdb.add_user("uuu3", "User4", "useremail4@server")
        self.assertIsNotNone(self.clientdb.get_user_id_by_uuid("uuu3"))

    def test_add_flow(self):
        self.assertIsNone(self.clientdb.get_flow_id_by_uuid("fff4"))
        self.clientdb.add_flow("fff4", "Chat4")
        self.assertIsNotNone(self.clientdb.get_flow_id_by_uuid("fff4"))

    def test_add_message(self):
        self.assertEqual(len(list(self.clientdb.list_messages(self.clientdb.get_flow_id_by_uuid("fff3")))), 1)
        self.clientdb.add_message("mmm4", "Message 4 in chat3 from user2", 10004,
                                  self.clientdb.get_user_id_by_uuid("uuu2"),
                                  self.clientdb.get_flow_id_by_uuid("fff3"))
        self.assertEqual(len(list(self.clientdb.list_messages(self.clientdb.get_flow_id_by_uuid("fff3")))), 2)

    def test_list_flow(self):
        self.assertEqual(len(list(self.clientdb.list_flow())), 3)

    def test_list_messages(self):
        self.assertEqual(len(list(self.clientdb.list_messages(self.clientdb.get_flow_id_by_uuid("fff1")))), 2)
        self.assertEqual(len(list(self.clientdb.list_messages(self.clientdb.get_flow_id_by_uuid("fff2")))), 0)
        self.assertEqual(len(list(self.clientdb.list_messages(self.clientdb.get_flow_id_by_uuid("fff3")))), 1)

    def test_get_user_id_by_uuid(self):
        self.assertIsNotNone(self.clientdb.get_user_id_by_uuid("uuu2"))
        self.assertIsNone(self.clientdb.get_user_id_by_uuid("uuu3"))

    def test_get_user_uuid_by_id(self):
        self.assertEqual(self.clientdb.get_user_id_by_uuid("uuu1"), 1)

    def test_get_flow_id_by_uuid(self):
        self.assertIsNotNone(self.clientdb.get_flow_id_by_uuid("fff3"))
        self.assertIsNone(self.clientdb.get_flow_id_by_uuid("fff4"))

    def test_get_flow_uuid_by_id(self):
        self.assertEqual(self.clientdb.get_flow_id_by_uuid("fff1"), 1)

    def test_get_param(self):
        self.assertEqual(self.clientdb.get_param("ExistParam", "[Value not set]"), "ExistParamValue")
        self.assertEqual(self.clientdb.get_param("NotExistParam", "[Value not set]"), "[Value not set]")

    def test_set_param(self):
        self.clientdb.set_param("NewParam", "NewParamValue")
        self.assertEqual(self.clientdb.get_param("NewParam", "[Value not set]"), "NewParamValue")

    def test_delete_param(self):
        self.clientdb.delete_param("ExistParam")
        self.assertEqual(self.clientdb.get_param("ExistParam", "[Value not set]"), "[Value not set]")
