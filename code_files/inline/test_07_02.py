import unittest
from unittest.mock import patch
import pre_07_02
import ref_07_02

class TestCheckerGame(unittest.TestCase):
    @patch('builtins.print')
    def test_pre_play_checker_game(self, mock_print):
        pre_07_02.main()
        expected_calls = [
            unittest.mock.call('   A B C D E F G H'),
            unittest.mock.call('  -----------------'),
            unittest.mock.call('1 |X   X   X   X | 1'),
            unittest.mock.call('2 |  X   X   X   X| 2'),
            unittest.mock.call('3 |X   X   X   X | 3'),
            unittest.mock.call('4 |  X   X   X   X| 4'),
            unittest.mock.call('5 |X   X   X   X | 5'),
            unittest.mock.call('6 |  X   X   X   X| 6'),
            unittest.mock.call('7 |X   X   X   X | 7'),
            unittest.mock.call('8 |  X   X   X   X| 8'),
            unittest.mock.call('  -----------------'),
            unittest.mock.call('   A B C D E F G H'),
            unittest.mock.call('   A B C D E F G H'),
            unittest.mock.call('  -----------------'),
            unittest.mock.call('1 |  X   X   X   X| 1'),
            unittest.mock.call('2 |X   X   X   X | 2'),
            unittest.mock.call('3 |X   X   X   X | 3'),
            unittest.mock.call('4 |  X   X   X   X| 4'),
            unittest.mock.call('5 |X   X   X   X | 5'),
            unittest.mock.call('6 |  X   X   X   X| 6'),
            unittest.mock.call('7 |X   X   X   X | 7'),
            unittest.mock.call('8 |  X   X   X   X| 8'),
            unittest.mock.call('  -----------------'),
            unittest.mock.call('   A B C D E F G H')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.print')
    def test_ref_play_checker_game(self, mock_print):
        ref_07_02.main()
        expected_calls = [
            unittest.mock.call('   A B C D E F G H'),
            unittest.mock.call('  -----------------'),
            unittest.mock.call('1 |X   X   X   X | 1'),
            unittest.mock.call('2 |  X   X   X   X| 2'),
            unittest.mock.call('3 |X   X   X   X | 3'),
            unittest.mock.call('4 |  X   X   X   X| 4'),
            unittest.mock.call('5 |X   X   X   X | 5'),
            unittest.mock.call('6 |  X   X   X   X| 6'),
            unittest.mock.call('7 |X   X   X   X | 7'),
            unittest.mock.call('8 |  X   X   X   X| 8'),
            unittest.mock.call('  -----------------'),
            unittest.mock.call('   A B C D E F G H'),
            unittest.mock.call('   A B C D E F G H'),
            unittest.mock.call('  -----------------'),
            unittest.mock.call('1 |  X   X   X   X| 1'),
            unittest.mock.call('2 |X   X   X   X | 2'),
            unittest.mock.call('3 |X   X   X   X | 3'),
            unittest.mock.call('4 |  X   X   X   X| 4'),
            unittest.mock.call('5 |X   X   X   X | 5'),
            unittest.mock.call('6 |  X   X   X   X| 6'),
            unittest.mock.call('7 |X   X   X   X | 7'),
            unittest.mock.call('8 |  X   X   X   X| 8'),
            unittest.mock.call('  -----------------'),
            unittest.mock.call('   A B C D E F G H')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()