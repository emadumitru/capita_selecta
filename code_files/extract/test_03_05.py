import unittest
from pre_03_05 import calculate_checksum as pre_calculate_checksum, generate_data as pre_generate_data, main as pre_main
from ref_03_05 import calculate_checksum as ref_calculate_checksum, generate_data as ref_generate_data, main as ref_main

class TestChecksum(unittest.TestCase):
    def test_pre_calculate_checksum(self):
        data = pre_generate_data()
        expected_checksum = pre_calculate_checksum(data)
        self.assertEqual(pre_calculate_checksum(data), expected_checksum)

    def test_ref_calculate_checksum(self):
        data = ref_generate_data()
        expected_checksum = ref_calculate_checksum(data)
        self.assertEqual(ref_calculate_checksum(data), expected_checksum)

    def test_pre_main(self):
        data = pre_generate_data()
        expected_checksum = pre_calculate_checksum(data)
        self.assertEqual(pre_main(), expected_checksum)

    def test_ref_main(self):
        data = ref_generate_data()
        expected_checksum = ref_calculate_checksum(data)
        self.assertEqual(ref_main(), expected_checksum)

if __name__ == '__main__':
    unittest.main()
