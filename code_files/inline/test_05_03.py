import unittest
import datetime
from pre_05_03 import convert_date as pre_convert_date
from ref_05_03 import convert_date as ref_convert_date

class TestDateConversion(unittest.TestCase):
    def test_pre_refactored_code(self):
        # Test today
        today = datetime.date.today()
        self.assertEqual(pre_convert_date("today"), today.strftime("%Y-%m-%d"))
        
        # Test tomorrow
        tomorrow = today + datetime.timedelta(days=1)
        self.assertEqual(pre_convert_date("tomorrow"), tomorrow.strftime("%Y-%m-%d"))
        
        # Test yesterday
        yesterday = today - datetime.timedelta(days=1)
        self.assertEqual(pre_convert_date("yesterday"), yesterday.strftime("%Y-%m-%d"))
        
        # Test specific date
        self.assertEqual(pre_convert_date("March 5, 2022"), "2022-03-05")
        
        # Test invalid date format
        self.assertEqual(pre_convert_date("Invalid date"), "Invalid date format")
    
    def test_refactored_code(self):
        # Test today
        today = datetime.date.today()
        self.assertEqual(ref_convert_date("today"), today.strftime("%Y-%m-%d"))
        
        # Test tomorrow
        tomorrow = today + datetime.timedelta(days=1)
        self.assertEqual(ref_convert_date("tomorrow"), tomorrow.strftime("%Y-%m-%d"))
        
        # Test yesterday
        yesterday = today - datetime.timedelta(days=1)
        self.assertEqual(ref_convert_date("yesterday"), yesterday.strftime("%Y-%m-%d"))
        
        # Test specific date
        self.assertEqual(ref_convert_date("March 5, 2022"), "2022-03-05")
        
        # Test invalid date format
        self.assertEqual(ref_convert_date("Invalid date"), "Invalid date format")

if __name__ == '__main__':
    unittest.main()
