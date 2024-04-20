import unittest
from unittest.mock import patch
import pre_09_05
import ref_09_05

class TestWordFrequency(unittest.TestCase):
    @patch('builtins.print')
    def test_pre_word_frequency(self, mock_print):
        pre_09_05.word_frequency_counter("This is a test. This is only a test.")
        expected_calls = [
            unittest.mock.call('this: 2'),
            unittest.mock.call('is: 2'),
            unittest.mock.call('a: 2'),
            unittest.mock.call('test: 2'),
            unittest.mock.call('only: 1')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.print')
    def test_ref_word_frequency(self, mock_print):
        result = ref_09_05.word_frequency_counter("This is a test. This is only a test.")
        for word, freq in result:
            print(f"{word}: {freq}")
        expected_calls = [
            unittest.mock.call('this: 2'),
            unittest.mock.call('is: 2'),
            unittest.mock.call('a: 2'),
            unittest.mock.call('test: 2'),
            unittest.mock.call('only: 1')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()