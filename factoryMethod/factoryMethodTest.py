import unittest.test
from factoryMethod.pessoa import PersonFactory, Customer, Employee

__author__ = 'Bruno'


class Test(unittest.TestCase):

    def test_customer(self):
        customer = PersonFactory().build_person("customer")
        customer.name = "Bruno"
        customer.say_hello()
        self.assertTrue(isinstance(customer, Customer))

    def test_employee(self):
        employee = PersonFactory().build_person("employee")
        employee.name = "Jarvis"
        employee.say_hello()
        self.assertTrue(isinstance(employee, Employee))

if __name__ == '__main__':
    unittest.main()
