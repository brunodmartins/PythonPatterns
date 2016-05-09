import platform
'''
Created on 09/05/2016

@author: bruno.martins
'''

class Desktop(object):
    '''
    classdocs
    '''    
    desktop = None;
    
    def __init__(self):
        self.system = platform.platform()
        self.release = platform.release()
    
    def __new__(self):
        if(Desktop.desktop == None):
            Desktop.desktop = object.__new__(Desktop)
        return Desktop.desktop 
        
    @classmethod
    def instance(cls):
        if(cls.desktop == None):
            cls.desktop = Desktop()
        return cls.desktop