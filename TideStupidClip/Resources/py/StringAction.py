'''
Created on 29/06/2014

@author: bgh
'''

from Action import Action
class StringAction(Action):
    '''
    Action that matches with string
    '''
    def __init__ (self, command, *matchers):
        """
        Command: command to execute
        matchers: string(s) to match
        """
        self.matchers = []
        for m in matchers:
            self.matchers.append(m.lower())
        Action.__init__(self, command)
    
    def matches(self, s):
        return s in self.matchers