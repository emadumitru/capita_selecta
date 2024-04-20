import unittest
import datetime

from pre_05_03 import convert_date as pre_convert_date
from ref_05_03 import convert_date as ref_convert_date

class TestDateConversion(unittest.TestCase):
    def test_pre_refactored_code(self):
        # Test today
        natural_date = "today"
        expected_date = datetime.date.today().strftime("%Y-%m-%d")
        self.assertEqual(pre_convert_date(natural_date), expected_date)

        # Test tomorrow
        natural_date = "tomorrow"
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        expected_date = tomorrow.strftime("%Y-%m-%d")
        self.assertEqual(pre_convert_date(natural_date), expected_date)

        # Test yesterday
        natural_date = "yesterday"
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        expected_date = yesterday.strftime("%Y-%m-%d")
        self.assertEqual(pre_convert_date(natural_date), expected_date)

        # Test custom date
        natural_date = "March 5, 2022"
        expected_date = "2022-03-05"
        self.assertEqual(pre_convert_date(natural_date), expected_date)

        # Test invalid date format
        natural_date = "Invalid date"
        expected_date = "Invalid date format"
        self.assertEqual(pre_convert_date(natural_date), expected_date)

    def test_refactored_code(self):
        # Test today
        natural_date = "today"
        expected_date = datetime.date.today().strftime("%Y-%m-%d")
        self.assertEqual(ref_convert_date(natural_date), expected_date)

        # Test tomorrow
        natural_date = "tomorrow"
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        expected_date = tomorrow.strftime("%Y-%m-%d")
        self.assertEqual(ref_convert_date(natural_date), expected_date)

        # Test yesterday
        natural_date = "yesterday"
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        expected_date = yesterday.strftime("%Y-%m-%d")
        self.assertEqual(ref_convert_date(natural_date), expected_date)

        # Test custom date
        natural_date = "March 5, 2022"
        expected_date = "2022-03-05"
        self.assertEqual(ref_convert_date(natural_date), expected_date)

        # Test invalid date format
        natural_date = "Invalid date"
        expected_date = "Invalid date format"
        self.assertEqual(ref_convert_date(natural_date), expected_date)

if __name__ == '__main__':
    unittest.main()
