import unittest
import hashlib
from pre_03_01 import calculate_checksum
from ref_03_01 import main as ref_main

class TestChecksum(unittest.TestCase):
    def test_pre_refactored_code(self):
        data = "Hello, world!"
        expected_checksum = hashlib.md5(data.encode('utf-8')).hexdigest()
        self.assertEqual(calculate_checksum(data), expected_checksum)

    def test_refactored_code(self):
        data = "Hello, world!"
        expected_checksum = hashlib.md5(data.encode('utf-8')).hexdigest()
        ref_main()
        self.assertEqual(ref_main(), expected_checksum)

if __name__ == '__main__':
    unittest.main()
