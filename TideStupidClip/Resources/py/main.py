class MainClass:
    
    def __init__(self):
        from action_manager import ActionManager
        self.action_manager = ActionManager()
        from MessageManager import MessageManager
        self.message_manager = MessageManager()
        self._dirty_add_actions()
    
    def get_new_messages (self):
        return self.message_manager.get_new_messages()
    
    def get_all_messages (self, n = None):
        return self.message_manager.get_all_messages(n)
        
    def execute_command(self, cmd):
        self.action_manager.execute(cmd)
    
    def _get_time(self):
        from datetime import datetime
        now = datetime.now()
        s = now.strftime("%H:%S")
        from Message import Message
        m = Message(s,"System")
        self.message_manager.add(m)
    
    def _dirty_add_actions(self):
        from StringAction import StringAction
        act = StringAction(self._get_time,"Dame la hora")
        self.action_manager.add(act)
