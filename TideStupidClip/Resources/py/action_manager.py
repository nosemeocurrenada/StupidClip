class ActionManager ():
    def __init__(self):
        self.actions = []
    
    def add(self,act):
        from Action import Action
        if not isinstance(act, Action):
            raise TypeError("act parameter (1) should be instance of Action")
        self.actions.append(act)
    
    def execute (self, s):
        self._match (s).execute()    
    
    def _match (self,s):
        res = []
        for action in self.actions:
            if action.matches (s):
                res.append(action)
        if len(res) > 1:
            # Should put an ambuiguity message in the bag
            raise Error("Ambiguity")
        if len(res) == 1:
            return res [0]
        # Should put an not found message in the bag
        return None 