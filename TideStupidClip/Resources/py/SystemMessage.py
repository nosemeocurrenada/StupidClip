from Message import Message
class SystemMessage(Message):
    def __init__(self,message):
        Message.__init__(self,message,"System")