import unittest
from pre_03_03 import generate_data as pre_generate_data, calculate_checksum as pre_calculate_checksum, display_checksum as pre_display_checksum
from ref_03_03 import main as ref_main

class TestChecksum(unittest.TestCase):
    def test_checksum(self):
        pre_data = pre_generate_data()
        pre_checksum = pre_calculate_checksum(pre_data)

        ref_main()

        # Capture the output of the refactored code
        captured_output = self.capsys.readouterr()

        # Extract the data and checksum from the captured output
        ref_output = captured_output.out.strip().split('\n')
        ref_data = list(map(int, ref_output[0].split(':')[1].strip().split()))
        ref_checksum = int(ref_output[1].split(':')[1].strip())

        # Compare the data and checksum
        self.assertEqual(pre_data, ref_data)
        self.assertEqual(pre_checksum, ref_checksum)

if __name__ == '__main__':
    unittest.main()
