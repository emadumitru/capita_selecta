import unittest
import io
import sys
from pre_03_05 import calculate_checksum as pre_calculate_checksum, generate_data as pre_generate_data, main as pre_main
from ref_03_05 import calculate_sha256_checksum as ref_calculate_checksum, generate_data as ref_generate_data, main as ref_main

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
        captured_output = io.StringIO()
        sys.stdout = captured_output
        pre_main()
        sys.stdout = sys.__stdout__
        expected_output = "Checksum: " + pre_calculate_checksum(pre_generate_data()) + "\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_ref_main(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        ref_main()
        sys.stdout = sys.__stdout__
        expected_output = "Checksum: " + ref_calculate_checksum(ref_generate_data()) + "\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
