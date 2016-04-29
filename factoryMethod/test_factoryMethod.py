import unittest
import pessoa

__author__ = 'Bruno'


class Test(unittest.TestCase):

    def test_customer(self):
        customer = pessoa.PersonFactory().build_person("customer")
        customer.name = "Bruno"
        customer.say_hello()
        self.assertTrue(isinstance(customer, pessoa.Customer))

    def test_employee(self):
        employee = pessoa.PersonFactory().build_person("employee")
        employee.name = "Jarvis"
        employee.say_hello()
        self.assertTrue(isinstance(employee, pessoa.Employee))

if __name__ == '__main__':
    unittest.main()
