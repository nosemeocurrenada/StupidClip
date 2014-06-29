from datetime import datetime, timedelta
class MainClass:
    
    def __init__(self, dir):
        from action_manager import ActionManager
        self.action_manager = ActionManager()
        from MessageManager import MessageManager
        self.message_manager = MessageManager()
        self._dirty_add_actions()
        self.tasks = []
    
    def get_new_messages (self):
        return self.message_manager.get_new_messages()
    
    def get_all_messages (self, n = None):
        return self.message_manager.get_all_messages(n)
        
    def execute_command(self, cmd):
        from UserMessage import UserMessage
        self.message_manager.add(UserMessage(cmd))
        self.action_manager.execute(cmd)
    
    def _get_time(self):
        now = datetime.now()
        s = now.strftime("%H:%S")
        from SystemMessage import SystemMessage
        m = SystemMessage(s)
        self.message_manager.add(m)
    
    def _add_task(self):
        t = datetime.now() + timedelta(seconds = 5)
        from UserMessage import UserMessage
        m = UserMessage("Che, no te duermas.")
        task = {'time':t,'message':m}
        self.tasks.append(task)
        self.message_manager.add(UserMessage("Ok, te aviso en 5s"))
        
    def update(self):
        for task in self.tasks:
            if datetime.now() > task["time"]:
                self.message_manager.add(task["message"])
    
    def _dirty_add_actions(self):
        from StringAction import StringAction
        act = StringAction(self._get_time,"Dame la hora")
        self.action_manager.add(act)
        act = StringAction(self._add_task,"Recordame")
        self.action_manager.add(act)
