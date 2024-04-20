import unittest
from unittest.mock import patch
import pre_08_03
import ref_08_03

class TestColorConversion(unittest.TestCase):
    @patch('builtins.print')
    def test_pre_color_conversion(self, mock_print):
        pre_08_03.convert_color("#FF0000")
        pre_08_03.convert_color("255,0,0")
        expected_calls = [
            unittest.mock.call('Hex code #FF0000 converted to RGB: (255, 0, 0)'),
            unittest.mock.call('RGB code 255,0,0 converted to Hex: #ff0000')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.print')
    def test_ref_color_conversion(self, mock_print):
        ref_08_03.convert_color_code("#FF0000")
        ref_08_03.convert_color_code("255,0,0")
        expected_calls = [
            unittest.mock.call('Hex code #FF0000 converted to RGB: (255, 0, 0)'),
            unittest.mock.call('RGB code 255,0,0 converted to Hex: #ff0000')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()