'''
Created on 28/04/2016

@author: bruno.martins
'''
import unittest
from shipyard import *


class Test(unittest.TestCase):


    def test01(self):
        battleFishingBoat = BattleFishingBoat()
        battleWarBoat = BattleWarBoat()
        captain = Captain(battleFishingBoat)
        captain.move()
        battleFishingBoat.move()
        captain.fire()
        battleFishingBoat.fire()
        captain = Captain(battleWarBoat)
        captain.move()
        battleWarBoat.move()
        captain.fire()
        battleWarBoat.fire() 
        
if __name__ == '__main__':
    unittest.main()

        
        
        