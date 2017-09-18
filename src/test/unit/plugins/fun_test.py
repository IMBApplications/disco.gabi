import unittest

from src.gabi.fun import *
from src.test.unit.plugins.utils import ChatMessageStub


class TestGroovyCommand(unittest.TestCase):
    def setUp(self):
        self.cmd = GroovyCommand()
        self.msg = ChatMessageStub()

    def test_groovy_command_without_user(self):
        self.cmd.on_execute(self.msg)

        self.assertEqual("Groovy? Did i hear groovy? I am groovy!", self.msg.response)

    def test_groovy_command_with_user(self):
        self.msg.msg = "looser"

        self.cmd.on_execute(self.msg)

        self.assertEqual("Groovy? Did i hear groovy? looser is groovy!", self.msg.response)


class TestImbaCommand(unittest.TestCase):
    def setUp(self):
        self.cmd = ImbaCommand()
        self.msg = ChatMessageStub()

    def test_imba_command_without_user(self):
        self.cmd.on_execute(self.msg)

        self.assertEqual("I am IMBA!", self.msg.response)

    def test_imba_command_with_user(self):
        self.msg.msg = "looser"

        self.cmd.on_execute(self.msg)

        self.assertEqual("looser is IMBA!", self.msg.response)



