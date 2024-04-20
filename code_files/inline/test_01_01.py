import unittest
import pre_01_01
import ref_01_01

class TestCPUUsage(unittest.TestCase):
    def test_get_cpu_usage(self):
        pre_cpu_usage = pre_01_01.get_cpu_usage()
        ref_cpu_usage = ref_01_01.get_cpu_usage()
        self.assertEqual(pre_cpu_usage, ref_cpu_usage)

    def test_monitor_cpu_usage(self):
        # Redirect stdout to a StringIO object to capture the print output
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the monitor_cpu_usage function from both versions
        pre_01_01.monitor_cpu_usage()
        ref_01_01.monitor_cpu_usage()

        # Get the captured output
        pre_output = captured_output.getvalue()
        captured_output = StringIO()  # Reset the StringIO object
        sys.stdout = captured_output
        ref_01_01.monitor_cpu_usage()
        ref_output = captured_output.getvalue()

        # Assert that the output from both versions is the same
        self.assertEqual(pre_output, ref_output)

if __name__ == '__main__':
    unittest.main()
