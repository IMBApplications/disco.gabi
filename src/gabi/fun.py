from src.gabi.core import ChatMessage, ChatCommand

import random

class GroovyCommand(ChatCommand):
    def __init__(self):
        ChatCommand.__init__(self, "groovy")

    def on_execute(self, msg: ChatMessage):
        if len(msg.msg) > 0:
            response = 'Groovy? Did i hear groovy? {0} is groovy!'.format(msg.msg)
        else:
            response = 'Groovy? Did i hear groovy? I am groovy!'

        msg.reply(response)


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
        if len(msg.msg) > 0:
            response = '{0} is IMBA!'.format(msg.msg)
        else:
            response = 'I am IMBA!'

        msg.reply(str(response))
