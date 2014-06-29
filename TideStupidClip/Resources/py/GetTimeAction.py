from Action import Action
class GetTimeAction(Action):
    def __init__(self, message_manager):
        Action.__init__(self,self._get_time)
        self.name = "GetTimeAction" + str(self.uid)
        self.message_manager = message_manager
        
    def _get_time(self, *args):
        from datetime import datetime
        now = datetime.now()
        s = now.strftime("%H:%S")
        from SystemMessage import SystemMessage
        m = SystemMessage(s)
        self.message_manager.add(m)

    def matches(self, s):
        s = s.lower()
        h = ["dame", "dime", "decime"]
        for k in h:
            if k == s[:len(k)] and "hora" in s: 
                return True
        return False