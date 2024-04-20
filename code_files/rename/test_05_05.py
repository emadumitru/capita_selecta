import unittest
from pre_05_05 import convert_date as pre_convert_date
from ref_05_05 import convert_natural_date as ref_convert_date

class TestDateConversion(unittest.TestCase):
    def test_convert_date(self):
        # Test case 1: Today's date
        natural_date = "today"
        pre_result = pre_convert_date(natural_date)
        ref_result = ref_convert_date(natural_date)
        self.assertEqual(pre_result, ref_result)

        # Test case 2: Yesterday's date
        natural_date = "yesterday"
        pre_result = pre_convert_date(natural_date)
        ref_result = ref_convert_date(natural_date)
        self.assertEqual(pre_result, ref_result)

        # Test case 3: Tomorrow's date
        natural_date = "tomorrow"
        pre_result = pre_convert_date(natural_date)
        ref_result = ref_convert_date(natural_date)
        self.assertEqual(pre_result, ref_result)

        # Test case 4: Specific date
        natural_date = "May 5, 2022"
        pre_result = pre_convert_date(natural_date)
        ref_result = ref_convert_date(natural_date)
        self.assertEqual(pre_result, ref_result)

        # Test case 5: Invalid date format
        natural_date = "Invalid date"
        pre_result = pre_convert_date(natural_date)
        ref_result = ref_convert_date(natural_date)
        self.assertEqual(pre_result, ref_result)

if __name__ == '__main__':
    unittest.main()
