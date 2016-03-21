'''
Created on 21/03/2016

@author: bruno.martins
'''

import unittest.test
from builder import HeroBuilder



class Test(unittest.TestCase):
    '''
    classdocs
    '''
    
    def test_builder(self):
        hero = HeroBuilder().withName('Teste').withPowers('Slaving').build();
        print(hero.name)
        print(hero.powers)
        


Test().test_builder()