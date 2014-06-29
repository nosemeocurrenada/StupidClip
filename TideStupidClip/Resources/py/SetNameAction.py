from RegexAction import RegexAction
class SetNameAction(RegexAction):
    def __init__(self, main):
        RegexAction.__init__(self,self._set_name)
        self.name = "SetNameAction" + str(self.uid)
        self.message_manager = main.message_manager
        self.main = main
        
    def _set_name(self, name):
        from SystemMessage import SystemMessage
        self.main.profile_set("name",name)
        s = "Un gusto, " + self.main.profile_get("name") + " :)"
        m = SystemMessage(s)
        self.message_manager.add(m)

    def matches(self, s):
        pattern = r'(?:Me llamo|Llamame|Mi nombre es) (\w*)'
        return RegexAction.matches(self,pattern,s)