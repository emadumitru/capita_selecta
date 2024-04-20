import unittest
from pre_01_01 import get_cpu_usage as pre_get_cpu_usage, monitor_cpu_usage as pre_monitor_cpu_usage
from ref_01_01 import get_cpu_usage as ref_get_cpu_usage, monitor_cpu_usage as ref_monitor_cpu_usage

class TestCPUUsage(unittest.TestCase):
    def test_get_cpu_usage(self):
        pre_cpu_usage = pre_get_cpu_usage()
        ref_cpu_usage = ref_get_cpu_usage()
        self.assertEqual(pre_cpu_usage, ref_cpu_usage)

    def test_monitor_cpu_usage(self):
        # Capture the output of the monitor_cpu_usage function
        import io
        from contextlib import redirect_stdout

        pre_output = io.StringIO()
        with redirect_stdout(pre_output):
            pre_monitor_cpu_usage()

        ref_output = io.StringIO()
        with redirect_stdout(ref_output):
            ref_monitor_cpu_usage()

        # Compare the output of the monitor_cpu_usage function
        self.assertEqual(pre_output.getvalue(), ref_output.getvalue())

if __name__ == '__main__':
    unittest.main()
