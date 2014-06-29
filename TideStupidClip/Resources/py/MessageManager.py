class MessageManager():
    def __init__(self):
        self.messages = []
        self.index = 0
    
    def add (self, message):
        from Message import Message
        if not isinstance(message, Message):
            raise TypeError("message parameter (1) should be instance of Message")
#        print "Agregando mensaje " + message.message
        self.messages.append(message)
#        print "Mensajes " + ",".join([m.message for m in self.messages])
        
    def get_new_messages (self):
        msg = self.messages[self.index:]
        self.index = len(self.messages)
#        print "New index set to " + str(self.index)
        return msg
    
    def get_all_messages (self, n = None):
        if not n: #It could be None
            n = 0
        return self.messages[-n:]