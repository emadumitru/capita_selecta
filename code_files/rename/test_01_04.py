import unittest
from pre_01_04 import get_cpu_usage as pre_get_cpu_usage, display_cpu_usage as pre_display_cpu_usage, monitor_cpu_usage as pre_monitor_cpu_usage
from ref_01_04 import get_cpu_usage as ref_get_cpu_usage, display_cpu_usage as ref_display_cpu_usage, monitor_and_display_cpu_usage as ref_monitor_and_display_cpu_usage

class TestCPUUsage(unittest.TestCase):
    def test_get_cpu_usage(self):
        pre_result = pre_get_cpu_usage()
        ref_result = ref_get_cpu_usage()
        self.assertEqual(pre_result, ref_result)

    def test_display_cpu_usage(self):
        cpu_usage = 50
        pre_display_output = pre_display_cpu_usage(cpu_usage)
        ref_display_output = ref_display_cpu_usage(cpu_usage)
        self.assertEqual(pre_display_output, ref_display_output)

    def test_monitor_cpu_usage(self):
        # Since the monitor_cpu_usage function runs indefinitely, we can only test it for a limited time.
        # Here, we will test it for 3 seconds and check if the outputs are the same.
        pre_output = []
        ref_output = []

        def pre_display_wrapper(cpu_usage):
            pre_output.append(cpu_usage)

        def ref_display_wrapper(cpu_usage):
            ref_output.append(cpu_usage)

        pre_monitor_cpu_usage(display_cpu_usage=pre_display_wrapper, sleep_time=1, max_duration=3)
        ref_monitor_and_display_cpu_usage(display_cpu_usage=ref_display_wrapper, sleep_time=1, max_duration=3)

        self.assertEqual(pre_output, ref_output)

if __name__ == '__main__':
    unittest.main()
