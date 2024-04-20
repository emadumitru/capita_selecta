import unittest
from unittest.mock import patch
import pre_07_01
import ref_07_01

class TestCheckerGame(unittest.TestCase):
    @patch('builtins.print')
    def test_pre_checker_game(self, mock_print):
        pre_07_01.play_checker_game()
        expected_calls = [
            unittest.mock.call('Welcome to the Checker Game!'),
            unittest.mock.call('Here is the initial board:'),
            unittest.mock.call(' '.join([' ' if (i+j) % 2 == 0 else 'X' for j in range(8)]) for i in range(8)),
            unittest.mock.call('Piece moved successfully!'),
            unittest.mock.call('Here is the updated board:'),
            unittest.mock.call(' '.join([' ' if (i+j) % 2 == 0 else 'X' for j in range(8)]) for i in range(8))
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.print')
    def test_ref_checker_game(self, mock_print):
        ref_07_01.play_checker_game()
        expected_calls = [
            unittest.mock.call('Welcome to the Checker Game!'),
            unittest.mock.call('Here is the initial board:'),
            unittest.mock.call(' '.join([' ' if (i+j) % 2 == 0 else 'X' for j in range(8)]) for i in range(8)),
            unittest.mock.call('Piece moved successfully!'),
            unittest.mock.call('Here is the updated board:'),
            unittest.mock.call(' '.join([' ' if (i+j) % 2 == 0 else 'X' for j in range(8)]) for i in range(8))
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()