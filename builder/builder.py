'''
Created on 21/03/2016

@author: bruno.martins
'''

class Hero(object):
    '''
    Hero class
    '''


    def __init__(self):
        '''
        Constructor
        '''

class HeroBuilder(object):
    
    
    def __init__(self):
        self.hero = Hero();
    
    def withPowers(self, power):
        self.hero.powers = power
        return self
    
    def withName(self, name):
        self.hero.name = name
        return self
    
    def build(self):
        return self.hero;