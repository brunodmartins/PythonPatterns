import abc
'''
Created on 10/05/2016

@author: bruno.martins
'''

class Processor(object):
    __metaclass__ = abc.ABCMeta
    '''
    classdocs
    '''
    def __init__(self, alu=None):
        '''
        Constructor
        '''
        self.alu = alu
    
    def sumTwoNumbers(self,number1, number2):
        print(self.alu.sum(number1,number2)) 

class AMDProcessor(Processor):
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''

class ALU(object):
    __metaclass__ = abc.ABCMeta
    
    
    def __init__(self):
        '''
        Constructor
        '''
    @abc.abstractmethod
    def sum(self,number1,number2):
        raise NotImplementedError

class AMDALU(object):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self):
        '''
        Constructor
        '''