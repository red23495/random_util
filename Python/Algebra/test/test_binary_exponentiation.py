import unittest
from ..binary_exponentiation import mod_pow


class BinaryExponentiationTest(unittest.TestCase):

    def test_calculates_power_properly(self):
        self.assertEqual(mod_pow(2, 2), 4)
        self.assertEqual(mod_pow(1, 10), 1)
        self.assertEqual(mod_pow(10, 5), 100000)
    
    def test_calculates_properly_for_big_result(self):
        self.assertEqual(mod_pow(10, 100000), 10**100000)
    
    def test_calculates_zero_when_base_is_zero(self):
        self.assertEqual(mod_pow(0, 10), 0)
    
    def test_calculates_one_when_power_is_zero(self):
        self.assertEqual(mod_pow(200, 0), 1)
    
    def test_calculates_positive_when_base_negative_and_pow_even(self):
        self.assertEqual(mod_pow(-2, 4), 16)
    
    def test_calculates_negative_when_base_negative_and_pow_odd(self):
        self.assertEqual(mod_pow(-2, 3), -8)
    
    def test_mods_result_properly_when_mod_given(self):
        self.assertEqual(mod_pow(2, 2, 1), 0)
        self.assertEqual(mod_pow(1, 10, 17), 1)
        self.assertEqual(mod_pow(10, 5, 15), 10)
        self.assertEqual(mod_pow(10, 5, 100001), 100000)