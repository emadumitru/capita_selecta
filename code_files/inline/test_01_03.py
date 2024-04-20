import unittest
from pre_01_03 import monitor_cpu_usage as pre_monitor_cpu_usage
from ref_01_03 import monitor_cpu_usage as ref_monitor_cpu_usage
import io
import sys

class TestCPUUsage(unittest.TestCase):
    def test_pre_refactored_code(self):
        # Redirect stdout to capture the output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call the pre-refactored code function
        pre_monitor_cpu_usage()

        # Get the captured output
        output = captured_output.getvalue()

        # Assert that the output contains the expected string
        self.assertIn("CPU Usage:", output)

    def test_refactored_code(self):
        # Redirect stdout to capture the output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        # Call the refactored code function
        ref_monitor_cpu_usage()

        # Get the captured output
        output = captured_output.getvalue()

        # Assert that the output contains the expected string
        self.assertIn("CPU Usage:", output)

if __name__ == '__main__':
    unittest.main()
