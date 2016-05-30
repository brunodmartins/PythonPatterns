"""
Created on 16/05/2016

@author: bruno.martins
"""
import abc


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

    """
    List files
    """
    @abc.abstractmethod
    def list_files(self):
        raise NotImplementedError


class Directory(File):
    
    def __init__(self, name):
        File.__init__(self, name)
        self.files = []

    """
    List files on this directory.
    """
    def list_files(self):
        print(self.name)
        for file in self.files:
            file.list_files()


class RegularFile(File):
    
    def __init__(self, name):
        File.__init__(self, name)

    def list_files(self):
        print(self.name)
