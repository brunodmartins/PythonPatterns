import abc
'''
Created on 22/04/2016

@author: bruno.martins
'''
from copy import copy


class Prototype(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def clone(self):
        raise NotImplementedError 
     
    

class Employee(Prototype):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.name = ''
        self.profession = ''
        self.language = ''
        
    def clone(self):
        return copy(self)
    
    def __str__(self, *args, **kwargs):
        return 'Name={} Professioin={} Language={}'.format(self.name, self.profession, self.language)
    
employee1 = Employee()
employee1.name = 'bruno'
employee1.profession = 'Dev' 
employee1.language = 'Java'
employee2 = employee1.clone()
employee2.name = 'Leh'
employee2.language = 'Php';
print(employee1)
print(employee2)