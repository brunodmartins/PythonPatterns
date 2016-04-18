import abc;
__author__ = 'Bruno'


class Person(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """Constructor"""
        self.name = ""

    @abc.abstractmethod
    def say_hello(self):
        """
        Say hello
        """
        raise NotImplementedError


class Employee(Person):

    def say_hello(self):
        """
        An employee hello
        """
        print("Hi, my name is " + self.name + " . How can I help you?")


class Customer(Person):

    def say_hello(self):
        """
        An customer hello
        """
        print("Hi, my name is " + self.name + " . I need someone help!")


class IPersonFactory(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def build_person(self, person_type):
        """Build a person"""
        raise NotImplementedError


class PersonFactory(IPersonFactory):

    def build_person(self, person_type):
        """Build a person"""
        if person_type.lower() == "customer":
            return Customer()
        else:
            return Employee()
