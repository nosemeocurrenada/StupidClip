'''
Created on 29/06/2014

@author: bgh
'''

class Action():
    '''
    classdocs
    '''


    def __init__(self, command):
        '''
        Constructor
            command : function to be called on execute ()
        '''
        self.command = command
    
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