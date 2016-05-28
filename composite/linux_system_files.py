'''
Created on 16/05/2016

@author: bruno.martins
'''
import abc;

class File(object):
    """
    classdocs
    """
    __metaclass__ = abc.ABCMeta 

    def __init__(self, name):
        """
        Constructor
        """
        self.name = name

class Directory(File):
    
    def __init__(self, name):
        super()._init__(name)
        self.files = []

class RegularFile(File):
    
    def __init__(self, name):
        super()._init__(name)
            