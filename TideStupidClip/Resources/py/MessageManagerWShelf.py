from MessageManager import MessageManager
class MessageManagerWShelf(MessageManager):
    def __init__(self,dir):
        MessageManager.__init__(self)
        import os
        path = os.path.join(dir,"messages.shelf")
#        print "Will open shelf at " + path
        from shelve import open
        self.shelf = open(path)
        
        for k in self.__dict__:
            if k != "shelf":
                self.__dict__[k] = self.shelf[k]
#                print "    loaded " + k + " = " + str(self.shelf[k])
        self.synchronize()

    def synchronize(self):
#        print "sync, before"
#        print "  shelf : " + str(self.shelf)
#        print "  self : " + str(self.__dict__)
        for k in self.__dict__:
            if k != "shelf":
                self.shelf[k] = self.__dict__[k]
#                print "    saved " + k + " = " + str(self.shelf[k])
#        print "sync, after"
#        print "  shelf : " + str(self.shelf)
#        print "  self : " + str(self.__dict__)
        self.shelf.sync()
    
    def add (self, message):
        MessageManager.add(self,message)
        self.synchronize()
#        print "AfterSync.Mensajes " + ",".join([m.message for m in self.messages])
        
    def get_new_messages (self):
        retval = MessageManager.get_new_messages(self)
        self.synchronize()
        return retval