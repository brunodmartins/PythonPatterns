"""
Created on 04/08/2016

@author: bruno.martins
"""
import abc


class ISecurityLogin:
    """
    ISecurityLogin interface
    """
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def login(self, name, pw, permission):
        """
        Do login
        :param name: User's name
        :param pw:  User's password
        :param permission:  User's permission
        """
        raise NotImplementedError
    

class SecurityLogin(ISecurityLogin):
    """
    SecurityLogin class implementing ISecurityLogin
    """

    def login(self, name, pw, permission):
        """
        Do login
        :param name: User's name
        :param pw:  User's password
        :param permission:  User's permission
        """
        print("Hello {}, you logged successfully!".format(name))


class SecurityLoginProxy(ISecurityLogin):
    """
    SecurityLogin's Proxy
    """
    
    securityLogin = SecurityLogin()
    
    def login(self, name, pw, permission=""):
        """
        Verify if a given user has permission to
        precede
        :param name: User's name
        :param pw:  User's password
        :param permission:  User's permission
        """
        if permission == "":
            raise Exception('Not authorized')
        else:
            self.securityLogin.login(name, pw, permission)
