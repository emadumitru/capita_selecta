import unittest
from unittest.mock import patch
import pre_07_05
import ref_07_05

class TestCheckerGame(unittest.TestCase):
    @patch('builtins.input', side_effect=['4', 'A', '3', 'B'])
    @patch('builtins.print')
    def test_pre_play_checker_game(self, mock_print, mock_input):
        pre_07_05.play_game()
        expected_calls = [
            unittest.mock.call('Welcome to the Peaceful Checker Game!'),
            unittest.mock.call('You can move your piece diagonally to an empty space.'),
            unittest.mock.call('The goal is to reach the opposite side of the board.'),
            unittest.mock.call('Let\'s start!'),
            unittest.mock.call('  A B C D E F G H'),
            unittest.mock.call('1 X   X   X   X '),
            unittest.mock.call('2   X   X   X   X'),
            unittest.mock.call('3 X   X   X   X '),
            unittest.mock.call('4   X   X   X   X'),
            unittest.mock.call('5 X   X   X   X '),
            unittest.mock.call('6   X   X   X   X'),
            unittest.mock.call('7 X   X   X   X '),
            unittest.mock.call('8   X   X   X   X'),
            unittest.mock.call('  A B C D E F G H'),
            unittest.mock.call('1 X   X   X   X '),
            unittest.mock.call('2   X   X   X   X'),
            unittest.mock.call('3   X   X   X   X'),
            unittest.mock.call('4 X   X   X   X '),
            unittest.mock.call('5 X   X   X   X '),
            unittest.mock.call('6   X   X   X   X'),
            unittest.mock.call('7 X   X   X   X '),
            unittest.mock.call('8   X   X   X   X')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.input', side_effect=['4', 'A', '3', 'B'])
    @patch('builtins.print')
    def test_ref_play_checker_game(self, mock_print, mock_input):
        ref_07_05.play_game()
        expected_calls = [
            unittest.mock.call('Welcome to the Peaceful Checker Game!'),
            unittest.mock.call('You can move your piece diagonally to an empty space.'),
            unittest.mock.call('The goal is to reach the opposite side of the board.'),
            unittest.mock.call('Let\'s start!'),
            unittest.mock.call('  A B C D E F G H'),
            unittest.mock.call('1 X   X   X   X '),
            unittest.mock.call('2   X   X   X   X'),
            unittest.mock.call('3 X   X   X   X '),
            unittest.mock.call('4   X   X   X   X'),
            unittest.mock.call('5 X   X   X   X '),
            unittest.mock.call('6   X   X   X   X'),
            unittest.mock.call('7 X   X   X   X '),
            unittest.mock.call('8   X   X   X   X'),
            unittest.mock.call('  A B C D E F G H'),
            unittest.mock.call('1 X   X   X   X '),
            unittest.mock.call('2   X   X   X   X'),
            unittest.mock.call('3   X   X   X   X'),
            unittest.mock.call('4 X   X   X   X '),
            unittest.mock.call('5 X   X   X   X '),
            unittest.mock.call('6   X   X   X   X'),
            unittest.mock.call('7 X   X   X   X '),
            unittest.mock.call('8   X   X   X   X')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()