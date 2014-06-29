from RegexAction import RegexAction
class GetTimeAction(RegexAction):
    def __init__(self, main):
        RegexAction.__init__(self,self._get_time)
        self.name = "GetTimeAction" + str(self.uid)
        self.message_manager = main.message_manager
        
    def _get_time(self, *args):
        from datetime import datetime
        now = datetime.now()
        s = now.strftime("%H:%S")
        from SystemMessage import SystemMessage
        m = SystemMessage(s)
        self.message_manager.add(m)

    def matches(self, s):
        pattern = r'(?:dime|decime|dame) (?:la hora|que hora es)'
        return RegexAction.matches(self,pattern,s)