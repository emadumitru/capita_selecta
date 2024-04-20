import unittest
from pre_01_04 import get_cpu_usage as pre_get_cpu_usage, display_cpu_usage as pre_display_cpu_usage, monitor_cpu_usage as pre_monitor_cpu_usage
from ref_01_04 import get_cpu_usage as ref_get_cpu_usage, display_cpu_usage as ref_display_cpu_usage, monitor_cpu_usage as ref_monitor_cpu_usage

class TestCPUUsage(unittest.TestCase):
    def test_get_cpu_usage(self):
        pre_cpu_usage = pre_get_cpu_usage()
        ref_cpu_usage = ref_get_cpu_usage()
        self.assertEqual(pre_cpu_usage, ref_cpu_usage)

    def test_display_cpu_usage(self):
        pre_cpu_usage = 50
        ref_cpu_usage = 50
        pre_display_cpu_usage(pre_cpu_usage)
        ref_display_cpu_usage(ref_cpu_usage)
        # Manually check the console output for correctness

    def test_monitor_cpu_usage(self):
        # Manually check the console output for correctness
        pre_monitor_cpu_usage()
        ref_monitor_cpu_usage()

if __name__ == '__main__':
    unittest.main()
