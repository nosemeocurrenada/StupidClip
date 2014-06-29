from RegexAction import RegexAction
class GetTaskAction(RegexAction):
    def __init__(self, main):
        RegexAction.__init__(self,self._get_task)
        self.name = "GetTaskAction" + str(self.uid)
        self.message_manager = main.message_manager
        self.todo_manager = main.todo_manager
        
    def _get_task(self):
        from SystemMessage import SystemMessage
        s = "Tenes que " + ",".join([t.message for t in self.todo_manager.tasks])
        m = SystemMessage(s)
        self.message_manager.add(m)

    def matches(self, s):
        pattern = r'^Que tengo (?:que hacer|pendiente(?: para hacer)*) *\?'
        return RegexAction.matches(self,pattern,s)