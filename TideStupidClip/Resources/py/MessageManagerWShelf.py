from MessageManager import MessageManager
class MessageManagerWShelf(MessageManager):
    def __init__(self,dir):
        MessageManager.__init__(self)
        from shelve import open
        self.shelf = open(dir + "messages.shelf")

    def synchronize(self):
        for k in self.__dict__:
            if k != "shelf":
                if self.shelf.has_key(k):
                    self.__dict__[k] = self.shelf[k]
                else:
                    self.shelf[k] = self.__dict__[k]