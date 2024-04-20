import unittest
from pre_05_04 import convert_date
from ref_05_04 import convert_natural_date_to_formatted_date

class TestDateConversion(unittest.TestCase):
    def test_convert_date(self):
        # Test case 1: Valid natural date
        natural_date = 'The 5th of April 2022'
        expected_result = '2022-04-05'
        self.assertEqual(convert_date(natural_date), expected_result)

        # Test case 2: Invalid natural date
        natural_date = 'Invalid date'
        expected_result = None
        self.assertEqual(convert_date(natural_date), expected_result)

    def test_convert_natural_date_to_formatted_date(self):
        # Test case 1: Valid natural date
        natural_date = 'The 5th of April 2022'
        expected_result = '2022-04-05'
        self.assertEqual(convert_natural_date_to_formatted_date(natural_date), expected_result)

        # Test case 2: Invalid natural date
        natural_date = 'Invalid date'
        expected_result = None
        self.assertEqual(convert_natural_date_to_formatted_date(natural_date), expected_result)

if __name__ == '__main__':
    unittest.main()
