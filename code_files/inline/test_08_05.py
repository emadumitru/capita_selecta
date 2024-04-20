import unittest
from unittest.mock import patch
import pre_08_05
import ref_08_05

class TestColorConversion(unittest.TestCase):
    @patch('builtins.print')
    def test_pre_color_conversion(self, mock_print):
        pre_08_05.main()
        expected_calls = [
            unittest.mock.call('RGB: (255, 0, 0)'),
            unittest.mock.call('Hexadecimal: #ff0000'),
            unittest.mock.call('Hexadecimal: #00ff00'),
            unittest.mock.call('RGB: (0, 255, 0)')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.print')
    def test_ref_color_conversion(self, mock_print):
        ref_08_05.color_converter()
        expected_calls = [
            unittest.mock.call('RGB: (255, 0, 0)'),
            unittest.mock.call('Hexadecimal: #ff0000'),
            unittest.mock.call('Hexadecimal: #00ff00'),
            unittest.mock.call('RGB: (0, 255, 0)')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()