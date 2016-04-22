'''
Created on 22/04/2016

@author: bruno.martins
'''
import unittest.test
from enterprise import Employee
from unittest.case import TestCase

class MyClass(TestCase):
    '''
    classdocs
    '''

    def test(self):
        employee1 = Employee()
        employee1.name = 'bruno'
        employee1.profession = 'Dev' 
        employee1.language = 'Java'
        employee2 = employee1.clone()
        employee2.name = 'Leh'
        employee2.language = 'Php'
        self.assertTrue(employee1.profession, 'Dev')
        self.assertTrue(employee2.profession, 'Dev')
        print(employee1)
        print(employee2)

        
if __name__ == '__main__':
    unittest.main()
