'''
Created on 04/08/2016

@author: bruno.martins
'''
import unittest
from ford import Fabric, Car


class Test(unittest.TestCase):

    def test_iterator(self):
        fabric = Fabric()
        fabric.cars.append(Car("Focus", "Black"))
        fabric.cars.append(Car("Ka", "Red"))
        fabric.cars.append(Car("Mustang", "Green"))
        iterator = fabric.getIterator()
        while iterator.hasNext():
            print(iterator.next())


if __name__ == "__main__":
    unittest.main()
