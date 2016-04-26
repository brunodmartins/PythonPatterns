'''
Created on 26/04/2016

@author: bruno.martins
'''
import abc

class Battleship(object):
    '''
    classdocs
    '''
    __metaclass__ = abc.ABCMeta;
    
    def fire(self):
        raise NotImplementedError
    
    def move(self):
        raise NotImplementedError

class Captain(Battleship):
    '''
    classdocs
    '''

    def __init__(self, battleship=None):
        '''
        Constructor
        '''
        self.battleship = battleship

    def fire(self):
        print 'Fire'
    
    def move(self):
        print 'Move'

class BattleFishingBoat(Battleship):
    '''
    classdocs
    '''
    
    def fire(self):
        print 'Fire'
    
    def move(self):
        print 'Move'

class FishihingBoat(object):
    '''
    classdocs
    '''
    
    def sail(self):
        print 'Sail'
    
    def fish(self):
        print 'Fish'
        