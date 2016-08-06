"""
Created on 04/08/2016

@author: bruno.martins
"""
import unittest
from proxy import security


class Test(unittest.TestCase):

    def testProxy(self):
        security_login = security.SecurityLoginProxy()
        security_login.login('Bruno', '123456', 'ADM')
        try:
            security_login.login('Bruno', '123456')
        except Exception as e:
            print(e)


if __name__ == "__main__":
    unittest.main()