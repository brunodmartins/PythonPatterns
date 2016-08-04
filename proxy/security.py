'''
Created on 04/08/2016

@author: bruno.martins
'''
import abc

class ISecurityLogin:
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def login(self, name, pw, permission):
        raise NotImplementedError
    

class SecurityLogin(ISecurityLogin):
    
    def login(self, name, pw, permission):
        print("Hello {}, you logged sucessfully!".format(name))

class SecurityLoginProxy(ISecurityLogin):
    
    securityLogin = SecurityLogin()
    
    def login(self, name, pw, permission=""):
        if permission == "":
            raise Exception('Not authorized')
        else:
            self.securityLogin.login(name, pw, permission)
        
