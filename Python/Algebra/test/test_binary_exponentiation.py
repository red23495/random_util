import unittest
from ..binary_exponentiation import bin_pow


class BinaryExponentiationTest(unittest.TestCase):

    def test_calculates_power_properly(self):
        self.assertEqual(bin_pow(2, 2), 4)
        self.assertEqual(bin_pow(1, 10), 1)
        self.assertEqual(bin_pow(10, 5), 100000)
    
    def test_calculates_properly_for_big_result(self):
        self.assertEqual(bin_pow(10, 100000), 10**100000)
    
    def test_calculates_zero_when_base_is_zero(self):
        self.assertEqual(bin_pow(0, 10), 0)
    
    def test_calculates_one_when_power_is_zero(self):
        self.assertEqual(bin_pow(200, 0), 1)
    
    def test_calculates_positive_when_base_negative_and_pow_even(self):
        self.assertEqual(bin_pow(-2, 4), 16)
    
    def test_calculates_negative_when_base_negative_and_pow_odd(self):
        self.assertEqual(bin_pow(-2, 3), -8)