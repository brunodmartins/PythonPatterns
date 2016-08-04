'''
Created on 04/08/2016

@author: bruno.martins
'''
import unittest
from flyweight import starbucks


class Test(unittest.TestCase):


    def testFlyWeight(self):
        starbucks.Orders.order_coffee("Weak", 2)
        starbucks.Orders.order_coffee("Strong", 3)
        starbucks.Orders.order_coffee("Weak", 5)
        starbucks.Orders.print_orders()
        orders = starbucks.Orders.orders
        assert orders[2] == orders[5]
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testFlyWeight']
    unittest.main()