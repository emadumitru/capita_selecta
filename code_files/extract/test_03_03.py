import unittest
from pre_03_03 import generate_data as pre_generate_data, calculate_checksum as pre_calculate_checksum, display_checksum as pre_display_checksum, main as pre_main
from ref_03_03 import generate_data as ref_generate_data, calculate_checksum as ref_calculate_checksum, display_checksum as ref_display_checksum, calculate_and_display_checksum as ref_calculate_and_display_checksum

class TestChecksum(unittest.TestCase):
    def test_generate_data(self):
        pre_data = pre_generate_data()
        ref_data = ref_generate_data()
        self.assertEqual(len(pre_data), len(ref_data))
        self.assertCountEqual(pre_data, ref_data)

    def test_calculate_checksum(self):
        pre_data = pre_generate_data()
        ref_data = ref_generate_data()
        pre_checksum = pre_calculate_checksum(pre_data)
        ref_checksum = ref_calculate_checksum(ref_data)
        self.assertEqual(pre_checksum, ref_checksum)

    def test_display_checksum(self):
        pre_data = pre_generate_data()
        ref_data = ref_generate_data()
        pre_checksum = pre_calculate_checksum(pre_data)
        ref_checksum = ref_calculate_checksum(ref_data)
        pre_display_checksum(pre_data, pre_checksum)
        ref_display_checksum(ref_data, ref_checksum)

    def test_main(self):
        pre_main()
        # No assertions needed as it only prints the output

    def test_calculate_and_display_checksum(self):
        ref_calculate_and_display_checksum()
        # No assertions needed as it only prints the output

if __name__ == '__main__':
    unittest.main()
