import unittest
from pre_03_04 import calculate_checksum as pre_calculate_checksum
from ref_03_04 import calculate_checksum as ref_calculate_checksum

class TestChecksum(unittest.TestCase):
    def test_pre_calculate_checksum(self):
        data = "Hello, world!"
        pre_md5_hash, pre_sha1_hash, pre_sha256_hash = pre_calculate_checksum(data)
        
        self.assertEqual(pre_md5_hash, "6cd3556deb0da54bca060b4c39479839")
        self.assertEqual(pre_sha1_hash, "2ef7bde608ce5404e97d5f042f95f89f1c232871")
        self.assertEqual(pre_sha256_hash, "5570b4f5b3b5a8f8d3c2e9f7eae7f2b23d64b1c7e98e8d548b73e08a1f7f5f6f")
    
    def test_ref_calculate_checksum(self):
        data = "Hello, world!"
        ref_md5_hash, ref_sha1_hash, ref_sha256_hash = ref_calculate_checksum(data)
        
        self.assertEqual(ref_md5_hash, "6cd3556deb0da54bca060b4c39479839")
        self.assertEqual(ref_sha1_hash, "2ef7bde608ce5404e97d5f042f95f89f1c232871")
        self.assertEqual(ref_sha256_hash, "5570b4f5b3b5a8f8d3c2e9f7eae7f2b23d64b1c7e98e8d548b73e08a1f7f5f6f")

if __name__ == '__main__':
    unittest.main()
