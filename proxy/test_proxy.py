'''
Created on 04/08/2016

@author: bruno.martins
'''
import unittest
from proxy import security


class Test(unittest.TestCase):


    def testProxy(self):
        securityLogin = security.SecurityLoginProxy()
        securityLogin.login('Bruno', '123456', 'ADM')
        try:
            securityLogin.login('Bruno', '123456')
        except Exception as e:
            print(e)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testProxy']
    unittest.main()