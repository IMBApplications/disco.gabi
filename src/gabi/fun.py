from src.gabi.core import ChatMessage, ChatCommand


class GroovyCommand(ChatCommand):
    def __init__(self):
        ChatCommand.__init__(self, "groovy")

    def on_execute(self, msg: ChatMessage):
        if len(msg.msg) > 0:
            response = 'Groovy? Did i hear groovy? {0} is groovy!'.format(msg.msg)
        else:
            response = 'Groovy? Did i hear groovy? I am groovy!'

        msg.reply(response)