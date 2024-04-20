import unittest
from pre_01_02 import get_cpu_usage as pre_get_cpu_usage, print_cpu_usage as pre_print_cpu_usage
from ref_01_02 import monitor_cpu_usage as ref_monitor_cpu_usage

class TestCPUUsage(unittest.TestCase):
    def test_get_cpu_usage(self):
        pre_cpu_usage = pre_get_cpu_usage()
        ref_cpu_usage = ref_monitor_cpu_usage()
        self.assertEqual(pre_cpu_usage, ref_cpu_usage)

    def test_print_cpu_usage(self):
        # Redirect stdout to a StringIO object to capture the print output
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        pre_print_cpu_usage()
        pre_output = captured_output.getvalue().strip()

        captured_output = StringIO()
        sys.stdout = captured_output

        ref_monitor_cpu_usage()
        ref_output = captured_output.getvalue().strip()

        sys.stdout = sys.__stdout__  # Restore stdout

        self.assertEqual(pre_output, ref_output)

if __name__ == '__main__':
    unittest.main()
