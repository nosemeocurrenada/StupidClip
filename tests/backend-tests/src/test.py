'''
Created on 29/06/2014

@author: bgh
'''
import interface
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        interface.init()

    def tearDown(self):
        pass

    def testGetsTime(self):
        interface.cmd("Dame la hora")
        messages = interface.get_new_msg()
        self.assertEqual(1, len(messages), "It should have only one message")
        from datetime import datetime
        self.assertTrue(type(messages[0]) is datetime, "Should return a date")

    def testGetsAllMessages(self):
        interface.cmd("Dame la hora")
        interface.cmd("Dame la hora")
        
        messages = interface.get_all_msg()
        self.assertEqual(2, len(messages), "There should be two messages")
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGetsTime']
    unittest.main()