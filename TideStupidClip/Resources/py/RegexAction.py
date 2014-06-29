from Action import Action
class RegexAction(Action):
    def __init__(self, command):
        Action.__init__(self,command)
        self.name = "RegexAction" + str(self.uid)
        
    def matches(self,pattern,s):
        import re
        if re.match(pattern,s,re.IGNORECASE):
            return True
        return False