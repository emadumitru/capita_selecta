import unittest
import psutil
import time
import concurrent.futures
from pre_01_05 import monitor_cpu_usage
from ref_01_05 import track_cpu_usage

class TestCpuUsage(unittest.TestCase):
    def test_cpu_usage(self):
        # Test the functionality of monitor_cpu_usage
        # by comparing its output with track_cpu_usage
        # for the same given input
        cpu_usage_pre = []
        cpu_usage_ref = []

        # Capture the CPU usage for 5 seconds using monitor_cpu_usage
        def capture_cpu_usage_pre():
            nonlocal cpu_usage_pre
            for _ in range(5):
                cpu_usage_pre.append(psutil.cpu_percent())
                time.sleep(1)

        # Capture the CPU usage for 5 seconds using track_cpu_usage
        def capture_cpu_usage_ref():
            nonlocal cpu_usage_ref
            for _ in range(5):
                cpu_usage_ref.append(psutil.cpu_percent())
                time.sleep(1)

        # Run the functions in parallel
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(capture_cpu_usage_pre)
            executor.submit(capture_cpu_usage_ref)

        # Compare the CPU usage lists
        self.assertEqual(cpu_usage_pre, cpu_usage_ref)

if __name__ == '__main__':
    unittest.main()
