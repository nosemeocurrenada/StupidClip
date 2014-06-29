from Message import Message
class UserMessage(Message):
    def __init__(self,message):
        Message.__init__(self,message,"User")