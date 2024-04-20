import unittest
from unittest.mock import patch
import pre_09_01
import ref_09_01

class TestWordFrequency(unittest.TestCase):
    @patch('builtins.print')
    def test_pre_word_frequency(self, mock_print):
        pre_09_01.main()
        expected_calls = [
            unittest.mock.call('Lorem: 1'),
            unittest.mock.call('ipsum: 1'),
            unittest.mock.call('dolor: 2'),
            unittest.mock.call('sit: 2'),
            unittest.mock.call('amet,: 2'),
            unittest.mock.call('consectetur: 1'),
            unittest.mock.call('adipiscing: 2'),
            unittest.mock.call('elit.: 1'),
            unittest.mock.call('Sed: 1'),
            unittest.mock.call('non: 1'),
            unittest.mock.call('risus.: 1'),
            unittest.mock.call('Suspendisse: 1'),
            unittest.mock.call('lectus: 1'),
            unittest.mock.call('tortor,: 1'),
            unittest.mock.call('dignissim: 1'),
            unittest.mock.call('nec,: 1'),
            unittest.mock.call('ultricies: 1'),
            unittest.mock.call('sed,: 1'),
            unittest.mock.call('dolor.: 1')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.print')
    def test_ref_word_frequency(self, mock_print):
        ref_09_01.main()
        expected_calls = [
            unittest.mock.call('Lorem: 1'),
            unittest.mock.call('ipsum: 1'),
            unittest.mock.call('dolor: 2'),
            unittest.mock.call('sit: 2'),
            unittest.mock.call('amet,: 2'),
            unittest.mock.call('consectetur: 1'),
            unittest.mock.call('adipiscing: 2'),
            unittest.mock.call('elit.: 1'),
            unittest.mock.call('Sed: 1'),
            unittest.mock.call('non: 1'),
            unittest.mock.call('risus.: 1'),
            unittest.mock.call('Suspendisse: 1'),
            unittest.mock.call('lectus: 1'),
            unittest.mock.call('tortor,: 1'),
            unittest.mock.call('dignissim: 1'),
            unittest.mock.call('nec,: 1'),
            unittest.mock.call('ultricies: 1'),
            unittest.mock.call('sed,: 1'),
            unittest.mock.call('dolor.: 1')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()