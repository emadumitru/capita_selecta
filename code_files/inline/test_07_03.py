import unittest
from unittest.mock import patch
import pre_07_03
import ref_07_03

class TestCheckerGame(unittest.TestCase):
    @patch('builtins.print')
    def test_pre_play_checker_game(self, mock_print):
        pre_07_03.play_game()
        expected_calls = [
            unittest.mock.call('Welcome to the Checker Game!'),
            unittest.mock.call('Here is the initial board:'),
            unittest.mock.call(' '.join([' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'])),
            unittest.mock.call(' '.join(['X', ' ', 'X', ' ', 'X', ' ', 'X', ' '])),
            unittest.mock.call(' '.join([' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'])),
            unittest.mock.call(' '.join(['X', ' ', 'X', ' ', 'X', ' ', 'X', ' '])),
            unittest.mock.call(' '.join([' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'])),
            unittest.mock.call(' '.join(['X', ' ', 'X', ' ', 'X', ' ', 'X', ' '])),
            unittest.mock.call(' '.join([' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'])),
            unittest.mock.call(' '.join(['X', ' ', 'X', ' ', 'X', ' ', 'X', ' '])),
            unittest.mock.call('Let\'s make a move!'),
            unittest.mock.call('Move successful!'),
            unittest.mock.call('Here is the updated board:'),
            unittest.mock.call(' '.join([' ', ' ', ' ', 'X', ' ', 'X', ' ', 'X'])),
            unittest.mock.call(' '.join(['X', ' ', 'X', ' ', 'X', ' ', 'X', ' '])),
            unittest.mock.call(' '.join([' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'])),
            unittest.mock.call(' '.join(['X', ' ', 'X', ' ', 'X', ' ', 'X', ' '])),
            unittest.mock.call(' '.join([' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'])),
            unittest.mock.call(' '.join(['X', ' ', 'X', ' ', 'X', ' ', 'X', ' '])),
            unittest.mock.call(' '.join([' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'])),
            unittest.mock.call(' '.join(['X', ' ', 'X', ' ', 'X', ' ', 'X', ' ']))
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.print')
    def test_ref_play_checker_game(self, mock_print):
        ref_07_03.play_game()
        expected_calls = [
            unittest.mock.call('Welcome to the Checker Game!'),
            unittest.mock.call('Here is the initial board:'),
            unittest.mock.call(' '.join([' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'])),
            unittest.mock.call(' '.join(['X', ' ', 'X', ' ', 'X', ' ', 'X', ' '])),
            unittest.mock.call(' '.join([' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'])),
            unittest.mock.call(' '.join(['X', ' ', 'X', ' ', 'X', ' ', 'X', ' '])),
            unittest.mock.call(' '.join([' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'])),
            unittest.mock.call(' '.join(['X', ' ', 'X', ' ', 'X', ' ', 'X', ' '])),
            unittest.mock.call(' '.join([' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'])),
            unittest.mock.call(' '.join(['X', ' ', 'X', ' ', 'X', ' ', 'X', ' '])),
            unittest.mock.call('Let\'s make a move!'),
            unittest.mock.call('Move successful!'),
            unittest.mock.call('Here is the updated board:'),
            unittest.mock.call(' '.join([' ', ' ', ' ', 'X', ' ', 'X', ' ', 'X'])),
            unittest.mock.call(' '.join(['X', ' ', 'X', ' ', 'X', ' ', 'X', ' '])),
            unittest.mock.call(' '.join([' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'])),
            unittest.mock.call(' '.join(['X', ' ', 'X', ' ', 'X', ' ', 'X', ' '])),
            unittest.mock.call(' '.join([' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'])),
            unittest.mock.call(' '.join(['X', ' ', 'X', ' ', 'X', ' ', 'X', ' '])),
            unittest.mock.call(' '.join([' ', 'X', ' ', 'X', ' ', 'X', ' ', 'X'])),
            unittest.mock.call(' '.join(['X', ' ', 'X', ' ', 'X', ' ', 'X', ' ']))
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()