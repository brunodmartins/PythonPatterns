"""
Created on 26/04/2016

@author: bruno.martins
"""
import abc


class Battleship(object):
    """
    classdocs
    """
    __metaclass__ = abc.ABCMeta;
    
    def fire(self):
        raise NotImplementedError
    
    def move(self):
        raise NotImplementedError


class Captain(Battleship):
    """
    classdocs
    """

    def __init__(self, battleship=None):
        '''
        Constructor
        '''
        self.battleship = battleship

    def fire(self):
        self.battleship.fire()
    
    def move(self):
        self.battleship.move()


class BattleFishingBoat(Battleship):
    """
    classdocs
    """

    def __init__(self):
        self.boat = FishihingBoat()

    def fire(self):
        print('Fire!')
    
    def move(self):
        self.boat.sail()


class FishihingBoat(object):
    """
    classdocs
    """
    
    def sail(self):
        print('The Boat is moving to that place')
    
    def fish(self):
        print('Fishing...')
