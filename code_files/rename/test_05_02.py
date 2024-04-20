import unittest
import datetime

from pre_05_02 import convert_date
from ref_05_02 import convert_natural_date_to_formatted_date

class TestDateConversion(unittest.TestCase):
    def test_convert_date(self):
        # Test case 1: Valid date format
        natural_date = "5th February 2022"
        expected_date = "2022-02-05"
        self.assertEqual(convert_date(natural_date), expected_date)

        # Test case 2: Invalid date format
        natural_date = "February 5th, 2022"
        expected_date = "Invalid date format"
        self.assertEqual(convert_date(natural_date), expected_date)

    def test_convert_natural_date_to_formatted_date(self):
        # Test case 1: Valid date format
        natural_date = "5th February 2022"
        expected_date = "2022-02-05"
        self.assertEqual(convert_natural_date_to_formatted_date(natural_date), expected_date)

        # Test case 2: Invalid date format
        natural_date = "February 5th, 2022"
        expected_date = "Invalid date format"
        self.assertEqual(convert_natural_date_to_formatted_date(natural_date), expected_date)

if __name__ == '__main__':
    unittest.main()
