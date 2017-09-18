class ChatMessage:
    def __init__(self, msg, sender, reply_function):
        self.msg = msg
        self.sender = sender
        self.__reply_function = reply_function

    def reply(self, msg):
        self.__reply_function(msg)

