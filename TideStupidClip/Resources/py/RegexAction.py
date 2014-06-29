from Action import Action
class RegexAction(Action):
    def __init__(self, command):
        Action.__init__(self,command)
        self.name = "RegexAction" + str(self.uid)
        
    def matches(self,pattern,s):
        import re
        result = re.match(pattern,s,re.IGNORECASE | re.MULTILINE)
        if result:
            self.command(*result.groups())
            return True
        return False
    
    def execute(self, *params):
        pass