import unittest
from pre_03_02 import calculate_checksum as pre_calculate_checksum
from ref_03_02 import calculate_checksum as ref_calculate_checksum, calculate_and_print_checksum

class TestChecksum(unittest.TestCase):
    def test_calculate_checksum(self):
        data = "Hello, world!"

        # Test the pre-refactored code
        pre_md5_checksum, pre_sha1_checksum, pre_sha256_checksum = pre_calculate_checksum(data)

        self.assertEqual(pre_md5_checksum, "6cd3556deb0da54bca060b4c39479839")
        self.assertEqual(pre_sha1_checksum, "2ef7bde608ce5404e97d5f042f95f89f1c232871")
        self.assertEqual(pre_sha256_checksum, "5570b4f5b3b5e7c1c16df6b6f2edc5b8b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5")

        # Test the refactored code
        ref_md5_checksum, ref_sha1_checksum, ref_sha256_checksum = ref_calculate_checksum(data)

        self.assertEqual(ref_md5_checksum, "6cd3556deb0da54bca060b4c39479839")
        self.assertEqual(ref_sha1_checksum, "2ef7bde608ce5404e97d5f042f95f89f1c232871")
        self.assertEqual(ref_sha256_checksum, "5570b4f5b3b5e7c1c16df6b6f2edc5b8b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5")

    def test_calculate_and_print_checksum(self):
        data = "Hello, world!"

        # Test the refactored code
        expected_output = "Data: Hello, world!\nMD5 Checksum: 6cd3556deb0da54bca060b4c39479839\nSHA1 Checksum: 2ef7bde608ce5404e97d5f042f95f89f1c232871\nSHA256 Checksum: 5570b4f5b3b5e7c1c16df6b6f2edc5b8b5b5b5b5b5b5b5b5b5b5b5b5b5b5b5"
        self.assertEqual(calculate_and_print_checksum(data), expected_output)

if __name__ == '__main__':
    unittest.main()
