import unittest
from pre_05_05 import convert_date as pre_convert_date
from ref_05_05 import convert_date as ref_convert_date

class TestConvertDate(unittest.TestCase):
    def test_pre_convert_date(self):
        self.assertEqual(pre_convert_date("today"), ref_convert_date("today"))
        self.assertEqual(pre_convert_date("yesterday"), ref_convert_date("yesterday"))
        self.assertEqual(pre_convert_date("tomorrow"), ref_convert_date("tomorrow"))
        self.assertEqual(pre_convert_date("May 5, 2022"), ref_convert_date("May 5, 2022"))
        self.assertEqual(pre_convert_date("Invalid date"), ref_convert_date("Invalid date"))

if __name__ == '__main__':
    unittest.main()
