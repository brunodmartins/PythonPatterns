import abc

__author__ = 'Bruno'


class Context:
    def __init__(self, input_text):
        self.input_text = input_text


class Expression:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def interpret(self, context):
        raise NotImplementedError


class NumberExpression(Expression):
    def __init__(self, number):
        self.number = number

    def interpret(self, context):
        return self.number


class PlusExpression(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)
