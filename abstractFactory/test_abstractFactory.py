import unittest
from abstractFactory.abstractFactory import GuiFactory,GnomeButton,KDEButton

__author__ = 'Bruno'


class Test(unittest.TestCase):

    def test_gnome(self):
        factory = GuiFactory.create_factory('Gnome')
        button = factory.create_button()
        self.assertTrue(isinstance(button, GnomeButton))

    def test_kde(self):
        factory = GuiFactory.create_factory('kde')
        button = factory.create_button()
        self.assertTrue(isinstance(button, KDEButton))

if __name__ == '__main__':
    unittest.main()
