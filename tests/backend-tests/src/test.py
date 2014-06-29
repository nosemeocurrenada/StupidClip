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
        self.assertEqual(2, len(messages), "It should have two messages")
        self.assertTrue("hola" in messages [1], "Should say hi")

    def testGetsAllMessages(self):
        interface.cmd("Dame la hora")
        interface.cmd("Dame la hora")
        
        messages = interface.get_all_msg()
        self.assertEqual(4, len(messages), "There should be four messages")
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testGetsTime']
    unittest.main()