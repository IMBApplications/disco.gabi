from src.gabi.core import ChatMessage


class ChatMessageStub(ChatMessage):
    def __init__(self):
        ChatMessage.__init__(self, "", "test_user", self.chat_reply)
        self.response = ""

    def chat_reply(self, msg_text):
        self.response = msg_text