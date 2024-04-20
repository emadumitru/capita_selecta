import unittest
from unittest.mock import patch
import pre_06_04
import ref_06_04

class TestTowerOfHanoi(unittest.TestCase):
    @patch('builtins.print')
    def test_pre_tower_of_hanoi(self, mock_print):
        pre_06_04.main()
        expected_calls = [
            unittest.mock.call('Solving Tower of Hanoi problem with 3 disks...'),
            unittest.mock.call('Move disk 1 from A to C'),
            unittest.mock.call('Move disk 2 from A to B'),
            unittest.mock.call('Move disk 1 from C to B'),
            unittest.mock.call('Move disk 3 from A to C'),
            unittest.mock.call('Move disk 1 from B to A'),
            unittest.mock.call('Move disk 2 from B to C'),
            unittest.mock.call('Move disk 1 from A to C'),
            unittest.mock.call('Tower of Hanoi problem solved!')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.print')
    def test_ref_solve_tower_of_hanoi(self, mock_print):
        ref_06_04.solve_tower_of_hanoi(3, "A", "B", "C")
        expected_calls = [
            unittest.mock.call('Solving Tower of Hanoi problem with 3 disks...'),
            unittest.mock.call('Move disk 1 from A to C'),
            unittest.mock.call('Move disk 2 from A to B'),
            unittest.mock.call('Move disk 1 from C to B'),
            unittest.mock.call('Move disk 3 from A to C'),
            unittest.mock.call('Move disk 1 from B to A'),
            unittest.mock.call('Move disk 2 from B to C'),
            unittest.mock.call('Move disk 1 from A to C'),
            unittest.mock.call('Tower of Hanoi problem solved!')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()