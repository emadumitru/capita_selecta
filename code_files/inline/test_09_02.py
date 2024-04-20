import unittest
from unittest.mock import patch
import pre_09_02
import ref_09_02

class TestWordFrequency(unittest.TestCase):
    @patch('builtins.print')
    def test_pre_word_frequency(self, mock_print):
        pre_09_02.word_frequency_counter("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
        pre_09_02.print_word_frequency(pre_09_02.word_frequency_counter("Lorem ipsum dolor sit amet, consectetur adipiscing elit."))
        expected_calls = [
            unittest.mock.call('lorem: 1'),
            unittest.mock.call('ipsum: 1'),
            unittest.mock.call('dolor: 1'),
            unittest.mock.call('sit: 1'),
            unittest.mock.call('amet: 1'),
            unittest.mock.call('consectetur: 1'),
            unittest.mock.call('adipiscing: 1'),
            unittest.mock.call('elit: 1')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.print')
    def test_ref_word_frequency(self, mock_print):
        ref_09_02.calculate_word_frequency("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
        expected_calls = [
            unittest.mock.call('lorem: 1'),
            unittest.mock.call('ipsum: 1'),
            unittest.mock.call('dolor: 1'),
            unittest.mock.call('sit: 1'),
            unittest.mock.call('amet: 1'),
            unittest.mock.call('consectetur: 1'),
            unittest.mock.call('adipiscing: 1'),
            unittest.mock.call('elit: 1')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()