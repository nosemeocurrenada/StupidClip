from RegexAction import RegexAction
class ReminderAction(RegexAction):
    """
    Relative remainder scheluder
    """
    def __init__(self, mainclass):
        RegexAction.__init__(self,self._schelude_task)
        self.name = "GetTimeAction" + str(self.uid)
        self.message_manager = mainclass.message_manager
        self.tasks = mainclass.tasks
        self.profile = mainclass.profile
        self.pattern = r'(?:avisame) (?:que|de) (\w+) en (\d+)(m| minutos|s| segundos)'
        
    def _schelude_task(self, action, number, unit):
        import re
        action, number, unit = re.match(self.pattern,args[0]).groups()
        
        from datetime import datetime, timedelta
        now = datetime.now()
        if re.match(r'\W(s|segundos)\W',unit):
            now += timedelta(seconds= number)
        if re.match(r'\W(m|minutos)\W',unit):
            now += timedelta(minutes= number)
        from SystemMessage import SystemMessage
        s = "Ok, te aviso a las " + now.strftime("%H:%S")
        m = SystemMessage(s)
        self.message_manager.add(m)
        
        t = datetime.now() + timedelta(seconds = 5)
        from SystemMessage import SystemMessage
        m = SystemMessage(self.profile["name"] + ", tenes que " + action + ".")
        task = {'time':t,'message':m}
        self.tasks.append(task)

    def matches(self, s):
        return RegexAction.matches(self,self.pattern,s)