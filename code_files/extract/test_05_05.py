import unittest
from pre_05_05 import convert_date as pre_convert_date
from ref_05_05 import convert_date as ref_convert_date

class TestDateConversion(unittest.TestCase):
    def test_pre_convert_date(self):
        # Test today
        self.assertEqual(pre_convert_date("today"), ref_convert_date("today"))
        
        # Test yesterday
        self.assertEqual(pre_convert_date("yesterday"), ref_convert_date("yesterday"))
        
        # Test tomorrow
        self.assertEqual(pre_convert_date("tomorrow"), ref_convert_date("tomorrow"))
        
        # Test specific date
        self.assertEqual(pre_convert_date("May 5, 2022"), ref_convert_date("May 5, 2022"))
        
        # Test invalid date format
        self.assertEqual(pre_convert_date("Invalid date"), ref_convert_date("Invalid date"))
        
    def test_ref_convert_date(self):
        # Test today
        self.assertEqual(ref_convert_date("today"), pre_convert_date("today"))
        
        # Test yesterday
        self.assertEqual(ref_convert_date("yesterday"), pre_convert_date("yesterday"))
        
        # Test tomorrow
        self.assertEqual(ref_convert_date("tomorrow"), pre_convert_date("tomorrow"))
        
        # Test specific date
        self.assertEqual(ref_convert_date("May 5, 2022"), pre_convert_date("May 5, 2022"))
        
        # Test invalid date format
        self.assertEqual(ref_convert_date("Invalid date"), pre_convert_date("Invalid date"))

if __name__ == '__main__':
    unittest.main()
