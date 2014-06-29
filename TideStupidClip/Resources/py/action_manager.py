class ActionManager ():
    def __init__(self, message_manager):
        self.actions = []
        self.message_manager = message_manager
    
    def add(self,act):
        from Action import Action
        if not isinstance(act, Action):
            raise TypeError("act parameter (1) should be instance of Action")
        self.actions.append(act)
    
    def execute (self, s):
        a = self._match (s)
        if a:
            a.execute(s)
            return True
        return False
    
    def _match (self,s):
        res = []
        for action in self.actions:
            if action.matches (s):
                res.append(action)
                
        from SystemMessage import SystemMessage
        if len(res) > 1:
            s = "A cual de los siguientes refiere?: " + "[" + ",".join([e.name for e in res]) + "]"
            m = SystemMessage(s)
            self.message_manager.add(m)
            return None
        if len(res) == 1:
            return res [0]
        self.message_manager.add (SystemMessage("No entiendo"))
        return None 