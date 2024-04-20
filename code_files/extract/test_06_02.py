import unittest
from unittest.mock import patch
import pre_06_02
import ref_06_02

class TestTowerOfHanoi(unittest.TestCase):
    @patch('builtins.print')
    def test_pre_tower_of_hanoi(self, mock_print):
        pre_06_02.complex_tower_of_hanoi(3)
        expected_calls = [
            unittest.mock.call('Initializing complex Tower of Hanoi...'),
            unittest.mock.call('Complex move disk 1 from A to C'),
            unittest.mock.call('Complex move disk 2 from A to B'),
            unittest.mock.call('Complex move disk 1 from C to B'),
            unittest.mock.call('Complex move disk 3 from A to C'),
            unittest.mock.call('Complex move disk 1 from B to A'),
            unittest.mock.call('Complex move disk 2 from B to C'),
            unittest.mock.call('Complex move disk 1 from A to C'),
            unittest.mock.call('Complex Tower of Hanoi completed!')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.print')
    def test_ref_tower_of_hanoi(self, mock_print):
        ref_06_02.complex_tower_of_hanoi(3)
        expected_calls = [
            unittest.mock.call('Initializing complex Tower of Hanoi...'),
            unittest.mock.call('Complex move disk 1 from A to C'),
            unittest.mock.call('Complex move disk 2 from A to B'),
            unittest.mock.call('Complex move disk 1 from C to B'),
            unittest.mock.call('Complex move disk 3 from A to C'),
            unittest.mock.call('Complex move disk 1 from B to A'),
            unittest.mock.call('Complex move disk 2 from B to C'),
            unittest.mock.call('Complex move disk 1 from A to C'),
            unittest.mock.call('Complex Tower of Hanoi completed!')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()