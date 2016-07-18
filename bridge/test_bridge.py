'''
Created on 07/07/2016

@author: bruno.martins
'''
import unittest
from bridge.computer import AMDProcessor, AmdAlu, IntelAlu


class Test(unittest.TestCase):


    def test_amd(self):
        amd_computer = AMDProcessor(AmdAlu())
        amd_computer.sum_two_numbers(1, 2)
        
    def test_intel(self):
        intel_computer = AMDProcessor(IntelAlu())
        intel_computer.sum_two_numbers(1, 2)
                
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()