import unittest
import hashlib
from pre_03_05 import calculate_checksum, generate_data
from ref_03_05 import main as ref_main

class TestChecksum(unittest.TestCase):
    def test_calculate_checksum(self):
        data = generate_data()
        expected_checksum = hashlib.sha256(data.encode()).hexdigest()
        actual_checksum = calculate_checksum(data)
        self.assertEqual(actual_checksum, expected_checksum)

    def test_main(self):
        data = generate_data()
        expected_checksum = hashlib.sha256(data.encode()).hexdigest()

        # Capture the output of the refactored code
        import sys
        from io import StringIO
        stdout = sys.stdout
        sys.stdout = StringIO()
        ref_main()
        ref_output = sys.stdout.getvalue().strip()
        sys.stdout = stdout

        # Check if the refactored code produces the same output
        self.assertEqual(ref_output, f"Checksum: {expected_checksum}")

if __name__ == '__main__':
    unittest.main()
