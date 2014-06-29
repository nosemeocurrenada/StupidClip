'''
Created on 29/06/2014

@author: bgh
'''
import unittest


class Test(unittest.TestCase):
    def f_stub(self):
        pass
    
    def setUp(self):
        from main import MainClass
        from SetNameAction import SetNameAction
        m = MainClass(None)
        m.sync = self.f_stub
        self.act = SetNameAction(m)


    def tearDown(self):
        pass


    def testCase1(self):
        choices = [#"Me llamo Maria,
                   #"Decime Carlos",
                   #"Dime Carlos",
                   "Llamame Carlos"
                   ]
        for s in choices:
            self.assertTrue(self.act.matches(s), s)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCase1']
    unittest.main()