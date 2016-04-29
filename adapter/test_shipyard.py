'''
Created on 28/04/2016

@author: bruno.martins
'''
import unittest
from adapter import shipyard


class Test(unittest.TestCase):


    def test01(self):
        battleFishingBoat = shipyard.BattleFishingBoat()
        battleWarBoat = shipyard.BattleWarBoat()
        captain = shipyard.Captain(battleFishingBoat)
        captain.move()
        battleFishingBoat.move()
        captain.fire()
        battleFishingBoat.fire()
        captain = shipyard.Captain(battleWarBoat)
        captain.move()
        battleWarBoat.move()
        captain.fire()
        battleWarBoat.fire() 
        
if __name__ == '__main__':
    unittest.main()

        
        
        