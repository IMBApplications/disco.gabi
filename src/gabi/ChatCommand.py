from src.gabi.ChatMessage import ChatMessage


class ChatCommand:
    def __init__(self, command_name):
        self.command_name = command_name

    def on_execute(self, msg: ChatMessage):
        pass

