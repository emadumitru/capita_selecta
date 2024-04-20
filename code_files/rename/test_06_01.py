import unittest
from unittest.mock import patch
import pre_06_01
import ref_06_01

class TestTowerOfHanoi(unittest.TestCase):
    @patch('builtins.print')
    def test_pre_tower_of_hanoi(self, mock_print):
        num_disks = 3
        source_peg = "A"
        auxiliary_peg = "B"
        destination_peg = "C"
        pre_06_01.solve_tower_of_hanoi(num_disks, source_peg, auxiliary_peg, destination_peg)
        expected_calls = [
            unittest.mock.call('Move disk 1 from peg A to peg C'),
            unittest.mock.call('Move disk 2 from peg A to peg B'),
            unittest.mock.call('Move disk 1 from peg C to peg B'),
            unittest.mock.call('Move disk 3 from peg A to peg C'),
            unittest.mock.call('Move disk 1 from peg B to peg A'),
            unittest.mock.call('Move disk 2 from peg B to peg C'),
            unittest.mock.call('Move disk 1 from peg A to peg C')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch('builtins.print')
    def test_ref_tower_of_hanoi(self, mock_print):
        num_disks = 3
        source_peg = "A"
        auxiliary_peg = "B"
        destination_peg = "C"
        ref_06_01.solve_tower_of_hanoi(num_disks, source_peg, auxiliary_peg, destination_peg)
        expected_calls = [
            unittest.mock.call('Move disk 1 from peg A to peg C'),
            unittest.mock.call('Move disk 2 from peg A to peg B'),
            unittest.mock.call('Move disk 1 from peg C to peg B'),
            unittest.mock.call('Move disk 3 from peg A to peg C'),
            unittest.mock.call('Move disk 1 from peg B to peg A'),
            unittest.mock.call('Move disk 2 from peg B to peg C'),
            unittest.mock.call('Move disk 1 from peg A to peg C')
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()