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
    def __init__(self, params):
        '''
        Constructor
        '''

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

class AMDALU(object):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self):
        '''
        Constructor
        '''