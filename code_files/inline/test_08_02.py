import unittest
from unittest.mock import patch
import pre_08_02
import ref_08_02

class TestColorConversion(unittest.TestCase):
    @patch('builtins.print')
    @patch('pre_08_02.generate_color_code', return_value='FF00FF')
    def test_pre_color_conversion(self, mock_generate_color_code, mock_print):
        pre_08_02.main()
        expected_calls = [
            unittest.mock.call('Generated Color Code: FF00FF'),
            unittest.mock.call('RGB: (255, 0, 255)'),
            unittest.mock.call('Converted Color Code: ff00ff')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.print')
    @patch('ref_08_02.generate_color_code', return_value='FF00FF')
    def test_ref_color_conversion(self, mock_generate_color_code, mock_print):
        ref_08_02.generate_and_convert_color()
        expected_calls = [
            unittest.mock.call('Generated Color Code: FF00FF'),
            unittest.mock.call('RGB: (255, 0, 255)'),
            unittest.mock.call('Converted Color Code: ff00ff')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()