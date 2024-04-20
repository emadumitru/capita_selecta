import unittest
import datetime

from pre_05_04 import convert_date as pre_convert_date
from ref_05_04 import convert_date as ref_convert_date

class TestConvertDate(unittest.TestCase):
    def test_pre_convert_date(self):
        # Test case 1: Valid natural date
        natural_date = 'The 5th of April 2022'
        expected_date = '2022-04-05'
        self.assertEqual(pre_convert_date(natural_date), expected_date)

        # Test case 2: Invalid natural date
        natural_date = 'Invalid date'
        self.assertIsNone(pre_convert_date(natural_date))

    def test_ref_convert_date(self):
        # Test case 1: Valid natural date
        natural_date = 'The 5th of April 2022'
        expected_date = '2022-04-05'
        self.assertEqual(ref_convert_date(natural_date), expected_date)

        # Test case 2: Invalid natural date
        natural_date = 'Invalid date'
        self.assertIsNone(ref_convert_date(natural_date))

if __name__ == '__main__':
    unittest.main()
