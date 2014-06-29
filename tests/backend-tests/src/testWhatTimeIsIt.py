'''
Created on 29/06/2014

@author: bgh
'''
import unittest
from GetTimeAction import GetTimeAction

class Test(unittest.TestCase):


    def setUp(self):
        self.act = GetTimeAction(None) # The message manager is used on execute(), we only test the matcher

    def tearDown(self):
        pass        
        
    def testCase1(self):
        s = "Dame la hora"
        self.assertTrue(self.act.matches(s), s)
    def testCase2(self):
        s = "Dime la hora"
        self.assertTrue(self.act.matches(s), s)
    def testCase3(self):
        s = "Decime la hora"
        self.assertTrue(self.act.matches(s), s)
    def testCase4(self):
        s = "Dame la caja"
        self.assertFalse(self.act.matches(s), s)
    def testCase5(self):
        s = "Dame la cahoraja"
        self.assertTrue(self.act.matches(s), s)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()