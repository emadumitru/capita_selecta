import unittest
from pre_03_01 import calculate_checksum as pre_calculate_checksum
from ref_03_01 import calculate_checksum as ref_calculate_checksum, calculate_and_print_checksum

class TestChecksum(unittest.TestCase):
    def test_pre_calculate_checksum(self):
        data = "Hello, world!"
        expected_checksum = "6cd3556deb0da54bca060b4c39479839"
        self.assertEqual(pre_calculate_checksum(data), expected_checksum)

    def test_ref_calculate_checksum(self):
        data = "Hello, world!"
        expected_checksum = "6cd3556deb0da54bca060b4c39479839"
        self.assertEqual(ref_calculate_checksum(data), expected_checksum)

    def test_calculate_and_print_checksum(self):
        data = "Hello, world!"
        expected_output = "Checksum: 6cd3556deb0da54bca060b4c39479839"
        self.assertEqual(calculate_and_print_checksum(data), expected_output)

if __name__ == '__main__':
    unittest.main()
