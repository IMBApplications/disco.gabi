import unittest

from src.test.unit.plugins.utils import ChatMessageStub
from src.gabi.hate import ShitCommand, AidsCommand, SihCommand
from src.gabi.core import ChatMessage


class TestShitCommand(unittest.TestCase):
    def setUp(self):
        self.cmd = ShitCommand()
        self.msg = ChatMessageStub()

    def test_shit_command_replies_holy_shit(self):
        self.cmd.on_execute(self.msg)

        self.assertEqual("Holy shit!", self.msg.response)


class TestAidsCommand(unittest.TestCase):
    def setUp(self):
        self.cmd = AidsCommand()
        self.msg = ChatMessageStub()

    def test_aids_command_without_user(self):
        self.cmd.on_execute(self.msg)

        self.assertEqual("test_user, who should get AIDS?", self.msg.response)

    def test_aids_command_with_user(self):
        self.msg.msg = "looser"

        self.cmd.on_execute(self.msg)

        self.assertEqual("looser, get AIDS!", self.msg.response)


class TestSihCommand(unittest.TestCase):
    def setUp(self):
        self.cmd = SihCommand()
        self.msg = ChatMessage("", "test_user", self.chat_reply)

    def chat_reply(self, msg_text):
        self.response = msg_text

    def test_sih_command_without_user(self):
        self.cmd.on_execute(self.msg)

        self.assertEqual("test_user, who should i shoot trough the throat?", self.response)

    def test_sih_command_with_user(self):
        self.msg.msg = "looser"

        self.cmd.on_execute(self.msg)

        self.assertEqual("looser, shoot trough your throat!", self.response)

