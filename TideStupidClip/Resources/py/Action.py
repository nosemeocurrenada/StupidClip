'''
Created on 29/06/2014

@author: bgh
'''

class Action():
    '''
    Clase base para las acciones
        command : funcion a ejecutar
        name : nombre para propositos de debug
        uid : id para propositos de debug
    '''
    uid = 0

    def __init__(self, command):
        '''
        Constructor
            command : function to be called on execute ()
        '''
        self.command = command
        self.uid = Action.uid
        Action.uid += 1
        self.name = "Action" + str(self.uid)
    
    def matches (self, s):
        """
        True if this Action matches the specified string
        """
        return False # Virtual
    
    def execute (self, *args):
        """
        Executes the command with the specified args
        """
        self.command(*args)