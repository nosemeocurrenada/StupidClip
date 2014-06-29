class TodoManager():
    def __init__(self):
        self.tasks = []
        
    def add(self, task):
        task.message    #La mejor manera de revisar una interfaz :D
        self.tasks.append(task)