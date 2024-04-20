import unittest
from pre_03_02 import calculate_checksum
from ref_03_02 import calculate_checksums

class TestChecksum(unittest.TestCase):
    def test_pre_refactored_code(self):
        data = "Hello, world!"
        expected_md5 = "6cd3556deb0da54bca060b4c39479839"
        expected_sha1 = "943a702d06f34599aee1f8da8ef9f7296031d699"
        expected_sha256 = "2ef7bde608ce5404e97d5f042f95f89f1c232871d"
        
        md5_checksum, sha1_checksum, sha256_checksum = calculate_checksum(data)
        
        self.assertEqual(md5_checksum, expected_md5)
        self.assertEqual(sha1_checksum, expected_sha1)
        self.assertEqual(sha256_checksum, expected_sha256)
    
    def test_refactored_code(self):
        data = "Hello, world!"
        expected_md5 = "6cd3556deb0da54bca060b4c39479839"
        expected_sha1 = "943a702d06f34599aee1f8da8ef9f7296031d699"
        expected_sha256 = "2ef7bde608ce5404e97d5f042f95f89f1c232871d"
        
        md5_checksum, sha1_checksum, sha256_checksum = calculate_checksums(data)
        
        self.assertEqual(md5_checksum, expected_md5)
        self.assertEqual(sha1_checksum, expected_sha1)
        self.assertEqual(sha256_checksum, expected_sha256)

if __name__ == '__main__':
    unittest.main()
