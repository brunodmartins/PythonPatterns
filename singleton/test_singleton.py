import unittest
from singleton.desktop import Desktop

__author__ = 'Bruno'


class Test(unittest.TestCase):

    def test_same_instaces(self):
        print('Desktop(), Desktop()')
        self.assertEqual(Desktop(), Desktop())
        print('Desktop.instance(), Desktop.instance()')
        self.assertEqual(Desktop.instance(), Desktop.instance())
        print('Desktop.instance(), Desktop()')
        self.assertEqual(Desktop.instance(), Desktop())

if __name__ == '__main__':
    unittest.main()
