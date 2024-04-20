import unittest
from unittest.mock import patch
import pre_09_03
import ref_09_03

class TestWordFrequency(unittest.TestCase):
    @patch('builtins.print')
    def test_pre_word_frequency(self, mock_print):
        pre_09_03.word_frequency_counter("This is a sample text. It contains some words that will be counted.")
        pre_09_03.print_word_frequency(pre_09_03.word_frequency_counter("This is a sample text. It contains some words that will be counted."))
        expected_calls = [
            unittest.mock.call('This: 1'),
            unittest.mock.call('is: 1'),
            unittest.mock.call('a: 1'),
            unittest.mock.call('sample: 1'),
            unittest.mock.call('text.: 1'),
            unittest.mock.call('It: 1'),
            unittest.mock.call('contains: 1'),
            unittest.mock.call('some: 1'),
            unittest.mock.call('words: 1'),
            unittest.mock.call('that: 1'),
            unittest.mock.call('will: 1'),
            unittest.mock.call('be: 1'),
            unittest.mock.call('counted.: 1')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.print')
    def test_ref_word_frequency(self, mock_print):
        ref_09_03.calculate_and_print_word_frequency("This is a sample text. It contains some words that will be counted.")
        expected_calls = [
            unittest.mock.call('This: 1'),
            unittest.mock.call('is: 1'),
            unittest.mock.call('a: 1'),
            unittest.mock.call('sample: 1'),
            unittest.mock.call('text.: 1'),
            unittest.mock.call('It: 1'),
            unittest.mock.call('contains: 1'),
            unittest.mock.call('some: 1'),
            unittest.mock.call('words: 1'),
            unittest.mock.call('that: 1'),
            unittest.mock.call('will: 1'),
            unittest.mock.call('be: 1'),
            unittest.mock.call('counted.: 1')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()