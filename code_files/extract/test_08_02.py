import unittest
from unittest.mock import patch
import pre_08_02
import ref_08_02

class TestColorConversion(unittest.TestCase):
    @patch('builtins.print')
    @patch('random.choice', return_value='F')
    def test_pre_color_conversion(self, mock_random, mock_print):
        pre_08_02.main()
        expected_calls = [
            unittest.mock.call('Generated Color Code: FFFFFF'),
            unittest.mock.call('RGB: (255, 255, 255)'),
            unittest.mock.call('Converted Color Code: ffffff')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.print')
    @patch('random.choice', return_value='F')
    def test_ref_color_conversion(self, mock_random, mock_print):
        ref_08_02.main()
        expected_calls = [
            unittest.mock.call('Generated Color Code: FFFFFF'),
            unittest.mock.call('RGB: (255, 255, 255)'),
            unittest.mock.call('Converted Color Code: ffffff')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()