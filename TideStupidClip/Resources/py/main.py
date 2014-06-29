class MainClass:
    
    def __init__(self):
        from action_manager import ActionManager
        self.action_manager = ActionManager()
        self.messages = []
        self.index = 0
        self._dirty_add_actions()
    
    def get_new_messages (self):
        msg = self.messages[self.index:]
        self.index = len(self.messages)
        return msg
    
    def get_all_messages (self, n = None):
        if not n: #It could be None
            n = 0
        return self.messages[-n:]
    
    def execute_command(self, cmd):
        self.action_manager.execute(cmd)
    
    def _get_time(self):
        from datetime import datetime
        now = datetime.now()
        s = now.strftime("%H:%S")
        self.messages.append(s)
    
    def _dirty_add_actions(self):
        from StringAction import StringAction
        act = StringAction(self._get_time,"Dame la hora")
        self.action_manager.add(act)
