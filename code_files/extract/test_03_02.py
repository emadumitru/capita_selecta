import unittest
from pre_03_02 import calculate_checksum as pre_calculate_checksum
from ref_03_02 import calculate_checksum as ref_calculate_checksum

class TestChecksum(unittest.TestCase):
    def test_pre_refactored_code(self):
        data = "Hello, world!"
        pre_md5_checksum, pre_sha1_checksum, pre_sha256_checksum = pre_calculate_checksum(data)

        self.assertEqual(pre_md5_checksum, "6cd3556deb0da54bca060b4c39479839")
        self.assertEqual(pre_sha1_checksum, "943a702d06f34599aee1f8da8ef9f7296031d699")
        self.assertEqual(pre_sha256_checksum, "2ef7bde608ce5404e97d5f042f95f89f1c2328712cc4b5d63beb7e64a80dd2")

    def test_refactored_code(self):
        data = "Hello, world!"
        ref_md5_checksum, ref_sha1_checksum, ref_sha256_checksum = ref_calculate_checksum(data)

        self.assertEqual(ref_md5_checksum, "6cd3556deb0da54bca060b4c39479839")
        self.assertEqual(ref_sha1_checksum, "943a702d06f34599aee1f8da8ef9f7296031d699")
        self.assertEqual(ref_sha256_checksum, "2ef7bde608ce5404e97d5f042f95f89f1c2328712cc4b5d63beb7e64a80dd2")

if __name__ == '__main__':
    unittest.main()
