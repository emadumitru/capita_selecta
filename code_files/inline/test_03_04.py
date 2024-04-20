import unittest
from pre_03_04 import calculate_checksum as pre_calculate_checksum
from ref_03_04 import calculate_checksum as ref_calculate_checksum

class TestChecksum(unittest.TestCase):
    def test_checksum(self):
        data = "Hello, world!"
        
        # Test the pre-refactored code
        pre_md5_hash, pre_sha1_hash, pre_sha256_hash = pre_calculate_checksum(data)
        self.assertEqual(pre_md5_hash, '6cd3556deb0da54bca060b4c39479839')
        self.assertEqual(pre_sha1_hash, '2ef7bde608ce5404e97d5f042f95f89f1c232871')
        self.assertEqual(pre_sha256_hash, 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e')
        
        # Test the refactored code
        ref_md5_hash, ref_sha1_hash, ref_sha256_hash = ref_calculate_checksum(data)
        self.assertEqual(ref_md5_hash, '6cd3556deb0da54bca060b4c39479839')
        self.assertEqual(ref_sha1_hash, '2ef7bde608ce5404e97d5f042f95f89f1c232871')
        self.assertEqual(ref_sha256_hash, 'a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e')

if __name__ == '__main__':
    unittest.main()
