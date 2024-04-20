import unittest
from unittest.mock import patch
import pre_08_04
import ref_08_04

class TestColorConversion(unittest.TestCase):
    @patch('builtins.print')
    def test_pre_color_conversion(self, mock_print):
        pre_08_04.main()
        expected_calls = [
            unittest.mock.call('RGB color:', (255, 0, 0)),
            unittest.mock.call('Hex color:', '#ff0000'),
            unittest.mock.call('Hex color:', '#00ff00'),
            unittest.mock.call('RGB color:', (0, 255, 0))
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.print')
    def test_ref_color_conversion(self, mock_print):
        ref_08_04.main()
        expected_calls = [
            unittest.mock.call('RGB color:', (255, 0, 0)),
            unittest.mock.call('Hex color:', '#ff0000'),
            unittest.mock.call('Hex color:', '#00ff00'),
            unittest.mock.call('RGB color:', (0, 255, 0))
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()