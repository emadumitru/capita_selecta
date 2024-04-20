import unittest
import datetime

from pre_05_02 import convert_date as pre_convert_date
from ref_05_02 import convert_date as ref_convert_date

class TestConvertDate(unittest.TestCase):
    def test_pre_convert_date(self):
        # Test a valid natural language date
        pre_natural_date = "5th February 2022"
        pre_expected_date = "2022-02-05"
        pre_actual_date = pre_convert_date(pre_natural_date)
        self.assertEqual(pre_actual_date, pre_expected_date)

        # Test an invalid natural language date
        pre_natural_date = "Invalid date"
        pre_expected_date = "Invalid date format"
        pre_actual_date = pre_convert_date(pre_natural_date)
        self.assertEqual(pre_actual_date, pre_expected_date)

    def test_ref_convert_date(self):
        # Test a valid natural language date
        ref_natural_date = "5th February 2022"
        ref_expected_date = "2022-02-05"
        ref_actual_date = ref_convert_date(ref_natural_date)
        self.assertEqual(ref_actual_date, ref_expected_date)

        # Test an invalid natural language date
        ref_natural_date = "Invalid date"
        ref_expected_date = "Invalid date format"
        ref_actual_date = ref_convert_date(ref_natural_date)
        self.assertEqual(ref_actual_date, ref_expected_date)

if __name__ == '__main__':
    unittest.main()
