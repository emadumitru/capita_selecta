import unittest
from unittest.mock import patch
import pre_07_04
import ref_07_04

class TestCheckersGame(unittest.TestCase):
    @patch('builtins.print')
    def test_pre_checkers_game(self, mock_print):
        board = pre_07_04.initialize_board()
        pre_07_04.print_board(board)
        expected_calls = [
            unittest.mock.call('   0  1  2  3  4  5  6  7'),
            unittest.mock.call('0 [X] [ ] [X] [ ] [X] [ ] [X] [ ] '),
            unittest.mock.call('1 [ ] [X] [ ] [X] [ ] [X] [ ] [X] '),
            unittest.mock.call('2 [X] [ ] [X] [ ] [X] [ ] [X] [ ] '),
            unittest.mock.call('3 [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] '),
            unittest.mock.call('4 [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] '),
            unittest.mock.call('5 [ ] [O] [ ] [O] [ ] [O] [ ] [O] '),
            unittest.mock.call('6 [O] [ ] [O] [ ] [O] [ ] [O] [ ] '),
            unittest.mock.call('7 [ ] [O] [ ] [O] [ ] [O] [ ] [O] ')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.print')
    def test_ref_checkers_game(self, mock_print):
        board = ref_07_04.create_checkerboard()
        ref_07_04.print_board(board)
        expected_calls = [
            unittest.mock.call('   0  1  2  3  4  5  6  7'),
            unittest.mock.call('0 [X] [ ] [X] [ ] [X] [ ] [X] [ ] '),
            unittest.mock.call('1 [ ] [X] [ ] [X] [ ] [X] [ ] [X] '),
            unittest.mock.call('2 [X] [ ] [X] [ ] [X] [ ] [X] [ ] '),
            unittest.mock.call('3 [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] '),
            unittest.mock.call('4 [ ] [ ] [ ] [ ] [ ] [ ] [ ] [ ] '),
            unittest.mock.call('5 [ ] [O] [ ] [O] [ ] [O] [ ] [O] '),
            unittest.mock.call('6 [O] [ ] [O] [ ] [O] [ ] [O] [ ] '),
            unittest.mock.call('7 [ ] [O] [ ] [O] [ ] [O] [ ] [O] ')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()