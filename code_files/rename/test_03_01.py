import unittest
from pre_03_01 import calculate_checksum as pre_calculate_checksum
from ref_03_01 import calculate_md5_checksum as ref_calculate_md5_checksum

class TestChecksum(unittest.TestCase):
    def test_pre_refactored_code(self):
        data = "Hello, world!"
        expected_checksum = "6cd3556deb0da54bca060b4c39479839"
        checksum = pre_calculate_checksum(data)
        self.assertEqual(checksum, expected_checksum)

    def test_refactored_code(self):
        data = "Hello, world!"
        expected_checksum = "6cd3556deb0da54bca060b4c39479839"
        checksum = ref_calculate_md5_checksum(data)
        self.assertEqual(checksum, expected_checksum)

if __name__ == '__main__':
    unittest.main()
