import unittest
from pre_03_04 import calculate_checksum as pre_calculate_checksum
from ref_03_04 import calculate_hashes as ref_calculate_hashes

class TestChecksum(unittest.TestCase):
    def test_pre_refactored_code(self):
        data = "Hello, world!"
        expected_md5 = "6cd3556deb0da54bca060b4c39479839"
        expected_sha1 = "943a702d06f34599aee1f8da8ef9f7296031d699"
        expected_sha256 = "2ef7bde608ce5404e97d5f042f95f89f1c232871df375"
        
        md5_hash, sha1_hash, sha256_hash = pre_calculate_checksum(data)
        
        self.assertEqual(md5_hash, expected_md5)
        self.assertEqual(sha1_hash, expected_sha1)
        self.assertEqual(sha256_hash, expected_sha256)
    
    def test_refactored_code(self):
        data = "Hello, world!"
        expected_md5 = "6cd3556deb0da54bca060b4c39479839"
        expected_sha1 = "943a702d06f34599aee1f8da8ef9f7296031d699"
        expected_sha256 = "2ef7bde608ce5404e97d5f042f95f89f1c232871df375"
        
        md5_hash, sha1_hash, sha256_hash = ref_calculate_hashes(data)
        
        self.assertEqual(md5_hash, expected_md5)
        self.assertEqual(sha1_hash, expected_sha1)
        self.assertEqual(sha256_hash, expected_sha256)

if __name__ == '__main__':
    unittest.main()
