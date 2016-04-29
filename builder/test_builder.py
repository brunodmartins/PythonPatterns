'''
Created on 21/03/2016

@author: bruno.martins
'''

import unittest
from builder import HeroBuilder



class Test(unittest.TestCase):
    '''
    classdocs
    '''
    
    def test_builder(self):
        hero = HeroBuilder().withName('Teste').withPowers('Slaving').build();
        print(hero.name)
        print(hero.powers)
        

if __name__ == '__main__':
    unittest.main()
