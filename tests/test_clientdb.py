from unittest import TestCase

from modules.database import clientdb

import sqlite3


class TestClientDb(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client_db = clientdb.ClientDb("sqlite:/:memory:")

    def setUp(self):
        self.client_db.create_db()
        self.client_db.add_user("uuu1", "User1", "useremail1@server")
        self.client_db.add_user("uuu2", "User2", "useremail2@server")
        self.client_db.add_flow("fff1", "Chat1")
        self.client_db.add_flow("fff2", "Chat2")
        self.client_db.add_flow("fff3", "Chat3")
        self.client_db.add_message("mmm1", "Message 1 in chat1 from user1", 10001,
                                  self.client_db.get_user_id_by_uuid("uuu1"),
                                  self.client_db.get_flow_id_by_uuid("fff1"))
        self.client_db.add_message("mmm2", "Message 2 in chat1 from user2", 10002,
                                  self.client_db.get_user_id_by_uuid("uuu2"),
                                  self.client_db.get_flow_id_by_uuid("fff1"))
        self.client_db.add_message("mmm3", "Message 3 in chat3 from user2", 10003,
                                  self.client_db.get_user_id_by_uuid("uuu2"),
                                  self.client_db.get_flow_id_by_uuid("fff3"))
        self.client_db.set_param("ExistParam", "ExistParamValue")

    def tearDown(self):
        self.client_db.delete_tables()

    def test_create_db(self):
        self.client_db.delete_tables()
        self.client_db.create_db()
        self.assertEqual(len(list(self.client_db.list_messages(self.client_db.get_flow_id_by_uuid("fff1")))), 0)
        self.assertEqual(len(list(self.client_db.list_messages(self.client_db.get_flow_id_by_uuid("fff3")))), 0)

    def test_delete_tables(self):
        self.client_db.delete_tables()
        self.assertIsNone(self.client_db.get_flow_id_by_uuid("fff1"))
        self.assertIsNone(self.client_db.get_user_id_by_uuid("uuu1"))

    def test_add_user(self):
        self.assertIsNone(self.client_db.get_user_id_by_uuid("uuu3"))
        self.client_db.add_user("uuu3", "User4", "useremail4@server")
        self.assertIsNotNone(self.client_db.get_user_id_by_uuid("uuu3"))

    def test_add_flow(self):
        self.assertIsNone(self.client_db.get_flow_id_by_uuid("fff4"))
        self.client_db.add_flow("fff4", "Chat4")
        self.assertIsNotNone(self.client_db.get_flow_id_by_uuid("fff4"))

    def test_add_message(self):
        self.assertEqual(len(list(self.client_db.list_messages(self.client_db.get_flow_id_by_uuid("fff3")))), 1)
        self.client_db.add_message("mmm4", "Message 4 in chat3 from user2", 10004,
                                  self.client_db.get_user_id_by_uuid("uuu2"),
                                  self.client_db.get_flow_id_by_uuid("fff3"))
        self.assertEqual(len(list(self.client_db.list_messages(self.client_db.get_flow_id_by_uuid("fff3")))), 2)

    def test_update_message(self):
        flow1 = self.client_db.get_flow_id_by_uuid("fff1")
        message = list(self.client_db.list_messages(flow1))[0]
        old_flow1_message = message.get('text')
        flow3 = self.client_db.get_flow_id_by_uuid("fff3")
        message = list(self.client_db.list_messages(flow3))[0]
        self.assertEqual(message.get('text'), 'Message 3 in chat3 from user2')
        self.client_db.update_message(message.get('uuid'), text='Edited text')
        message = list(self.client_db.list_messages(flow3))[0]
        self.assertEqual(message.get('text'), 'Edited text')
        flow1 = self.client_db.get_flow_id_by_uuid("fff1")
        message = list(self.client_db.list_messages(flow1))[0]
        self.assertEqual(message.get('text'), old_flow1_message)

    def test_list_flow(self):
        self.assertEqual(len(list(self.client_db.list_flow())), 3)

    def test_list_messages(self):
        self.assertEqual(len(list(self.client_db.list_messages(self.client_db.get_flow_id_by_uuid("fff1")))), 2)
        self.assertEqual(len(list(self.client_db.list_messages(self.client_db.get_flow_id_by_uuid("fff2")))), 0)
        self.assertEqual(len(list(self.client_db.list_messages(self.client_db.get_flow_id_by_uuid("fff3")))), 1)

    def test_get_user_id_by_uuid(self):
        self.assertIsNotNone(self.client_db.get_user_id_by_uuid("uuu2"))
        self.assertIsNone(self.client_db.get_user_id_by_uuid("uuu3"))

    def test_get_user(self):
        self.assertIsNone(self.client_db.get_user())
        self.assertIsNotNone(self.client_db.get_user(user_uuid="uuu2"))
        self.assertIsNone(self.client_db.get_user(user_uuid="uuu3"))
        self.assertIsNotNone(self.client_db.get_user(
            user_id=self.client_db.get_user_id_by_uuid("uuu2")))

    def test_get_flow(self):
        self.assertIsNone(self.client_db.get_flow())
        self.assertIsNotNone(self.client_db.get_flow(flow_uuid="fff3"))
        self.assertIsNone(self.client_db.get_flow(flow_uuid="fff4"))
        self.assertIsNotNone(self.client_db.get_flow(
            flow_id=self.client_db.get_flow_id_by_uuid("fff3")))

    def test_get_user_uuid_by_id(self):
        self.assertEqual(self.client_db.get_user_id_by_uuid("uuu1"), 1)

    def test_get_flow_id_by_uuid(self):
        self.assertIsNotNone(self.client_db.get_flow_id_by_uuid("fff3"))
        self.assertIsNone(self.client_db.get_flow_id_by_uuid("fff4"))

    def test_get_flow_uuid_by_id(self):
        self.assertEqual(self.client_db.get_flow_id_by_uuid("fff1"), 1)

    def test_get_param(self):
        self.assertEqual(self.client_db.get_param("ExistParam", "[Value not set]"), "ExistParamValue")
        self.assertEqual(self.client_db.get_param("NotExistParam", "[Value not set]"), "[Value not set]")

    def test_set_param(self):
        self.client_db.set_param("NewParam", "NewParamValue")
        self.assertEqual(self.client_db.get_param("NewParam", "[Value not set]"), "NewParamValue")

    def test_delete_param(self):
        self.client_db.delete_param("ExistParam")
        self.assertEqual(self.client_db.get_param("ExistParam", "[Value not set]"), "[Value not set]")
