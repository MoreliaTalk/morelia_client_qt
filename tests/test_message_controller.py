import unittest
import sys
from PyQt5.QtWidgets import QApplication

import main


class TestMessageController(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.mainWindow = main.MainWindow()
        self.mainWindow.show()

    def test_add_message(self):
        self.assertEqual(self.mainWindow.MessageController.add_message(
                            type="my", text="111111"
                        ),
                         self.mainWindow.MessageAreaContent.children()[-1])
        # sys.exit(self.app.exec_())


if __name__ == "__main__":
    unittest.main()
