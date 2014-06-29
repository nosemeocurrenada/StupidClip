from datetime import datetime, timedelta
class MainClass:
    
    def __init__(self, dir):
        self.message_manager = self._create_message_manager(None)
        from action_manager import ActionManager
        self.action_manager = ActionManager(self.message_manager)
        self._dirty_add_actions()
        self.tasks = []
        
        if dir:
            import os
            options_path = os.path.join(dir,"options.shelf")
            profile_path = os.path.join(dir,"profile.shelf")
            
            from shelve import open
            self.options = open(options_path)
            self.profile = open(profile_path)
            
            if not self.profile.has_key("name"):
                self.profile["name"] = "DefaultCarlos"
    
    def get_new_messages (self):
        return self.message_manager.get_new_messages()
    
    def get_all_messages (self, n = None):
        return self.message_manager.get_all_messages(n)
        
    def execute_command(self, cmd):
        from UserMessage import UserMessage
        self.message_manager.add(UserMessage(cmd))
        return self.action_manager.execute(cmd.lower())
        
    def _add_task(self, *args):
        t = datetime.now() + timedelta(seconds = 5)
        from UserMessage import UserMessage
        m = UserMessage(self.options["name"] + ", no te duermas.")
        task = {'time':t,'message':m}
        self.tasks.append(task)
        self.message_manager.add(UserMessage("Ok, te aviso en 5s"))
        
    def update(self):
        torem = []
        for task in self.tasks:
            if datetime.now() > task["time"]:
                self.message_manager.add(task["message"])
                torem.append(task)
                
        for task in torem:
            self.tasks.remove(task)

    def _set_name_to_carlos(self, *args):
        self.profile_set("name","Carlos")
        from UserMessage import UserMessage
        self.message_manager.add(UserMessage("Ok, ahora te llamas Carlos."))
    
    def _say_hi(self, *args):
        from UserMessage import UserMessage
        self.message_manager.add(UserMessage("Hola, " + self.profile["name"]))
    
    def _dirty_add_actions(self):
        from GetTimeAction import GetTimeAction
        from StringAction import StringAction
        act = GetTimeAction(self.message_manager)
        self.action_manager.add(act)
        act = StringAction(self._add_task,"Recordame","Recordarme","Recuerdame")
        self.action_manager.add(act)
        act = StringAction(self._set_name_to_carlos,"Dime Carlos")
        self.action_manager.add(act)
        act = StringAction(self._say_hi,"Hola")
        self.action_manager.add(act)


    def profile_set(self,key,value):
        self.profile[key] = value
        self.profile.sync()
    
    def profile_get(self,key):
        return self.profile[key]
    
    def options_set(self,key,value):
        self.options[key] = value
        self.options.sync()
        
    def options_get(self,key):
        return self.options[key]
    
    def _create_message_manager(self,dir):
        if dir:
            from MessageManagerWShelf import MessageManagerWShelf
            return MessageManagerWShelf(dir)
        from MessageManager import MessageManager
        print "Mensajes sin persistencia"
        return MessageManager()
    
if __name__ == "__main__":
    m = MainClass(".")
    m.execute_command("Dame la hora")
    for msg in m.get_all_messages():
        print msg.sender + ":" + msg.message