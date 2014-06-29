'''
Created on 29/06/2014

@author: bgh
'''
import interface
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        interface.init(None)

    def tearDown(self):
        pass

    def testSaysHi(self):
        interface.cmd("Hola")
        messages = interface.get_new_msg()
        #print [m.message for m in messages]
        self.assertEqual(2, len(messages), "It should have two messages, were " + str(len(messages)))
        self.assertTrue("hola" in messages [1].message.lower(), "Should say hi")

    def testGetsAllMessages(self):
        interface.cmd("Dame la hora")
        interface.cmd("Dame la hora")
        
        messages = interface.get_all_msg()
        print messages
        self.assertEqual(4, len(messages), "There should be four messages, were " + str(len(messages)))
        
    def testSetTodo(self):
        interface.cmd("Tengo que matar a flanders")
        interface.get_new_msg() # me resultan irrelevantes
        interface.cmd("Que tengo que hacer?")
        messages = interface.get_new_msg()
        print [e.message for e in messages]
        self.assertEqual("Tenes que matar a flanders", messages[1], "Debo matar a flanders")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGetsTime']
    unittest.main()