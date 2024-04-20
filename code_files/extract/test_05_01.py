import unittest
import datetime

from pre_05_01 import convert_date as pre_convert_date
from ref_05_01 import convert_date as ref_convert_date

class TestDateConversion(unittest.TestCase):
    def test_pre_refactored_code(self):
        # Test case 1: January 1, 2022
        natural_date = 'January 1, 2022'
        expected_date = '2022-01-01'
        self.assertEqual(pre_convert_date(natural_date), expected_date)

        # Test case 2: December 31, 2022
        natural_date = 'December 31, 2022'
        expected_date = '2022-12-31'
        self.assertEqual(pre_convert_date(natural_date), expected_date)

        # Test case 3: February 29, 2020 (leap year)
        natural_date = 'February 29, 2020'
        expected_date = '2020-02-29'
        self.assertEqual(pre_convert_date(natural_date), expected_date)

    def test_refactored_code(self):
        # Test case 1: January 1, 2022
        natural_date = 'January 1, 2022'
        expected_date = '2022-01-01'
        self.assertEqual(ref_convert_date(natural_date), expected_date)

        # Test case 2: December 31, 2022
        natural_date = 'December 31, 2022'
        expected_date = '2022-12-31'
        self.assertEqual(ref_convert_date(natural_date), expected_date)

        # Test case 3: February 29, 2020 (leap year)
        natural_date = 'February 29, 2020'
        expected_date = '2020-02-29'
        self.assertEqual(ref_convert_date(natural_date), expected_date)

if __name__ == '__main__':
    unittest.main()
