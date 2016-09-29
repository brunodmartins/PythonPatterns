'''
Created on 28/09/2016

@author: bruno
'''
import unittest
from interpreter.Calculator import Context, NumberExpression, PlusExpression


class Test(unittest.TestCase):
    """
    Test class
    """
    def test(self):
        """
        Test the interpret
        """
        context = Context("3+5")
        n1 = NumberExpression(3)
        n2 = NumberExpression(5)
        p = PlusExpression(n1, n2)
        assert 8 == p.interpret(context)

if __name__ == "__main__":
    unittest.main()
