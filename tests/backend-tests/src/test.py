'''
Created on 29/06/2014

@author: bgh
'''
import interface
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        interface.init(".")

    def tearDown(self):
        pass

    def testGetsTime(self):
        interface.cmd("Dame la hora")
        messages = interface.get_new_msg()
        self.assertEqual(2, len(messages), "It should have only one message")
        self.assertEqual(2, len(messages [1].message.split(":")), "Should return a date with format HH:MM")

    def testGetsAllMessages(self):
        interface.cmd("Dame la hora")
        interface.cmd("Dame la hora")
        
        messages = interface.get_all_msg()
        self.assertEqual(4, len(messages), "There should be two messages")
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGetsTime']
    unittest.main()