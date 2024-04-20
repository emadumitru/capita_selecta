import unittest
from unittest.mock import patch
import pre_09_04
import ref_09_04

class TestWordFrequency(unittest.TestCase):
    @patch('builtins.print')
    def test_pre_word_frequency(self, mock_print):
        pre_09_04.main()
        expected_calls = [
            unittest.mock.call('lorem: 1'),
            unittest.mock.call('ipsum: 1'),
            unittest.mock.call('dolor: 1'),
            unittest.mock.call('sit: 1'),
            unittest.mock.call('amet: 1'),
            unittest.mock.call('consectetur: 1'),
            unittest.mock.call('adipiscing: 1'),
            unittest.mock.call('elit: 1'),
            unittest.mock.call('sed: 2'),
            unittest.mock.call('semper: 1'),
            unittest.mock.call('nisl: 2'),
            unittest.mock.call('euismod: 1'),
            unittest.mock.call('nunc: 4'),
            unittest.mock.call('id: 2'),
            unittest.mock.call('aliquam: 1'),
            unittest.mock.call('lacinia: 2'),
            unittest.mock.call('tincidunt: 1'),
            unittest.mock.call('sem: 1'),
            unittest.mock.call('nec: 1')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.print')
    def test_ref_word_frequency(self, mock_print):
        ref_09_04.main()
        expected_calls = [
            unittest.mock.call('lorem: 1'),
            unittest.mock.call('ipsum: 1'),
            unittest.mock.call('dolor: 1'),
            unittest.mock.call('sit: 1'),
            unittest.mock.call('amet: 1'),
            unittest.mock.call('consectetur: 1'),
            unittest.mock.call('adipiscing: 1'),
            unittest.mock.call('elit: 1'),
            unittest.mock.call('sed: 2'),
            unittest.mock.call('semper: 1'),
            unittest.mock.call('nisl: 2'),
            unittest.mock.call('euismod: 1'),
            unittest.mock.call('nunc: 4'),
            unittest.mock.call('id: 2'),
            unittest.mock.call('aliquam: 1'),
            unittest.mock.call('lacinia: 2'),
            unittest.mock.call('tincidunt: 1'),
            unittest.mock.call('sem: 1'),
            unittest.mock.call('nec: 1')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()