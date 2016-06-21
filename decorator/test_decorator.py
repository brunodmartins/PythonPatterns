import unittest
from decorator.restaurant import *

__author__ = 'Bruno'


class Test(unittest.TestCase):
    def test_just_hamburger(self):
        hamburger = Hamburger()
        assert hamburger.price() == 5
        assert hamburger.description() == 'A Big Mac'

    def test_hamburger_with_everything(self):
        hamburger = SaladDecorator(BaconDecorator(CheeseDecorator(Hamburger())))
        assert hamburger.price() == 11
        assert hamburger.description() == 'A Big Mac, with cheese, with bacon, with salad'


if __name__ == '__main__':
    unittest.main()
