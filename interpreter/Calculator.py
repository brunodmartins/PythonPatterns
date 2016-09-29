"""
Calculator module
"""
import abc

__author__ = 'Bruno'


class Context:
    """
    Context'class
    """

    def __init__(self, input_text):
        """
        Constructor
        """
        self.input_text = input_text


class Expression:
    """
    Expression's class
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def interpret(self, context):
        """
        Interpret the Expression
        """
        raise NotImplementedError


class NumberExpression(Expression):
    """
    NumberExpression'class
    """

    def __init__(self, number):
        """
        Constructor
        """
        self.number = number

    def interpret(self, context):
        """
        Interpret the Expression
        """
        return self.number


class PlusExpression(Expression):
    """
    PlusExpression's class
    """

    def __init__(self, left, right):
        """
        Constructor
        """
        self.left = left
        self.right = right

    def interpret(self, context):
        """
        Interpret the Expression
        """
        return self.left.interpret(context) + self.right.interpret(context)
