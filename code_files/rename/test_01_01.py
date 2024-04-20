import unittest
from pre_01_01 import get_cpu_usage as pre_get_cpu_usage, monitor_cpu_usage as pre_monitor_cpu_usage
from ref_01_01 import get_cpu_usage as ref_get_cpu_usage, track_cpu_usage as ref_track_cpu_usage

class TestCPUUsage(unittest.TestCase):
    def test_get_cpu_usage(self):
        pre_cpu_usage = pre_get_cpu_usage()
        ref_cpu_usage = ref_get_cpu_usage()
        self.assertEqual(pre_cpu_usage, ref_cpu_usage)

    def test_monitor_cpu_usage(self):
        # Redirect stdout to a StringIO object to capture the print output
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        # Run the pre-refactored code
        pre_monitor_cpu_usage()

        # Get the output of the pre-refactored code
        pre_output = captured_output.getvalue().strip()

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Redirect stdout again to capture the print output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Run the refactored code
        ref_track_cpu_usage()

        # Get the output of the refactored code
        ref_output = captured_output.getvalue().strip()

        # Reset stdout
        sys.stdout = sys.__stdout__

        self.assertEqual(pre_output, ref_output)

if __name__ == '__main__':
    unittest.main()
