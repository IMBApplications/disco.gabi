from src.gabi.ChatCommand import ChatCommand, ChatMessage


class ShitCommand(ChatCommand):
    def __init__(self):
        ChatCommand.__init__(self, "shit")

    def on_execute(self, msg: ChatMessage):
        msg.reply("Holy shit!")


class AidsCommand(ChatCommand):
    def __init__(self):
        ChatCommand.__init__(self, "aids")

    def on_execute(self, msg: ChatMessage):
        if len(msg.msg) > 0:
            response = '{0}, get AIDS!'.format(msg.msg)
        else:
            response = '{0}, who should get AIDS?'.format(msg.sender)

        msg.reply(response)


class SihCommand(ChatCommand):
    def __init__(self):
        ChatCommand.__init__(self, "sih")

    def on_execute(self, msg: ChatMessage):
        if len(msg.msg) > 0:
            response = '{0}, shoot trough your throat!'.format(msg.msg)
        else:
            response = '{0}, who should i shoot trough the throat?'.format(msg.sender)

        msg.reply(response)
