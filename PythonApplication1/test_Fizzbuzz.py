import unittest
from fizzbuzz import *

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        for i in [3, 6, 9, 18]:
            print('testing', i)
            assert FizzBuzz.fizzbuzz(i) == 'Fizz'

    def test_buzz(self):
        for i in [5, 10, 20, 25]:
            print('testing', i)
            assert FizzBuzz.fizzbuzz(i) == 'Buzz'

    def test_fizzbuzz(self):
        for i in [15, 30, 45, 60]:
            print('testing', i)
            assert FizzBuzz.fizzbuzz(i) == 'FizzBuzz'

    def test_fizzbuzz_returns_int(self):
         for i in [4, 23, 67, 79]:
            print('testing', i)
            assert FizzBuzz.fizzbuzz(i) == i

    def test_getInput_returns_int(self):
        for i in ['3', '6', '9', '18']:
            print('testing', i)
            assert FizzBuzz.getInput(i) == int(i)

    def test_getInput_returns_error_if_not_an_int(self):
        vals = ["a", "1.28", "!?!"]
        for i in vals:
            print ('testing', i)
            with self.assertRaises(Exception): 
                FizzBuzz.getInput(i) == int(i)