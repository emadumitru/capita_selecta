import unittest
from unittest.mock import patch
import pre_07_05
import ref_07_05

class TestCheckersGame(unittest.TestCase):
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1', 'A', '2', 'B'])
    def test_pre_checkers_game(self, mock_input, mock_print):
        pre_07_05.play_game()
        expected_calls = [
            unittest.mock.call('Welcome to the Peaceful Checker Game!'),
            unittest.mock.call('You can move your piece diagonally to an empty space.'),
            unittest.mock.call('The goal is to reach the opposite side of the board.'),
            unittest.mock.call("Let's start!"),
            unittest.mock.call('  A B C D E F G H'),
            unittest.mock.call('1 X   X   X   X '),
            unittest.mock.call('2   X   X   X   X'),
            unittest.mock.call('3 X   X   X   X '),
            unittest.mock.call('4                 '),
            unittest.mock.call('5                 '),
            unittest.mock.call('6   X   X   X   X'),
            unittest.mock.call('7 X   X   X   X '),
            unittest.mock.call('8   X   X   X   X'),
            unittest.mock.call('  A B C D E F G H'),
            unittest.mock.call('1   X   X   X   X'),
            unittest.mock.call('2 X   X   X   X '),
            unittest.mock.call('3 X   X   X   X '),
            unittest.mock.call('4                 '),
            unittest.mock.call('5                 '),
            unittest.mock.call('6   X   X   X   X'),
            unittest.mock.call('7 X   X   X   X '),
            unittest.mock.call('8   X   X   X   X')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1', 'A', '2', 'B'])
    def test_ref_checkers_game(self, mock_input, mock_print):
        ref_07_05.play_game()
        expected_calls = [
            unittest.mock.call('Welcome to the Peaceful Checker Game!'),
            unittest.mock.call('You can move your piece diagonally to an empty space.'),
            unittest.mock.call('The goal is to reach the opposite side of the board.'),
            unittest.mock.call("Let's start!"),
            unittest.mock.call('  A B C D E F G H'),
            unittest.mock.call('1 X   X   X   X '),
            unittest.mock.call('2   X   X   X   X'),
            unittest.mock.call('3 X   X   X   X '),
            unittest.mock.call('4                 '),
            unittest.mock.call('5                 '),
            unittest.mock.call('6   X   X   X   X'),
            unittest.mock.call('7 X   X   X   X '),
            unittest.mock.call('8   X   X   X   X'),
            unittest.mock.call('  A B C D E F G H'),
            unittest.mock.call('1   X   X   X   X'),
            unittest.mock.call('2 X   X   X   X '),
            unittest.mock.call('3 X   X   X   X '),
            unittest.mock.call('4                 '),
            unittest.mock.call('5                 '),
            unittest.mock.call('6   X   X   X   X'),
            unittest.mock.call('7 X   X   X   X '),
            unittest.mock.call('8   X   X   X   X')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()