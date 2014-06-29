from RegexAction import RegexAction
class SetTaskAction(RegexAction):
    def __init__(self, main):
        RegexAction.__init__(self,self._set_task)
        self.name = "SetTaskAction" + str(self.uid)
        self.message_manager = main.message_manager
        self.todo_manager = main.todo_manager
        
    def _set_task(self, msg):
        from SystemMessage import SystemMessage
        answers = ["Me parece buena idea","Anotado"]
        import random
        s = random.choice(answers)
        m = SystemMessage(s)
        self.message_manager.add(m)
        
        from TodoTask import TodoTask
        self.todo_manager.add(TodoTask(msg))

    def matches(self, s):
        pattern = r'tengo que (.*)'
        return RegexAction.matches(self,pattern,s)