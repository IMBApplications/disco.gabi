import random

from src.gabi.core import ChatMessage, ChatCommand
from src.gabi.utils import user_targetet_reply


class GroovyCommand(ChatCommand):
    def __init__(self):
        ChatCommand.__init__(self, "groovy")

    def on_execute(self, msg: ChatMessage):
        user_targetet_reply('Groovy? Did i hear groovy? {0} is groovy!', 'Groovy? Did i hear groovy? I am groovy!', msg)


class RollCommand(ChatCommand):
    def __init__(self):
        ChatCommand.__init__(self, "roll")

    def on_execute(self, msg: ChatMessage):
        if len(msg.msg) > 0:
            response = random.randint(1, int(msg.msg))
        else:
            response = random.randint(1, 6)

        msg.reply(str(response))


class ImbaCommand(ChatCommand):
    def __init__(self):
        ChatCommand.__init__(self, "imba")

    def on_execute(self, msg: ChatMessage):
        user_targetet_reply('{0} is IMBA!', 'I am IMBA!', msg)
