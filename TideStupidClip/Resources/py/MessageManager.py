class MessageManager():
    def __init__(self):
        self.messages = []
        self.index = 0
    
    def add (self, message):
        from Message import Message
        if not isinstance(message, Message):
            raise TypeError("message parameter (1) should be instance of Message")
        self.messages.append(message)
        
    def get_new_messages (self):
        msg = self.messages[self.index:]
        self.index = len(self.messages)
        return msg
    
    def get_all_messages (self, n = None):
        if not n: #It could be None
            n = 0
        return self.messages[-n:]