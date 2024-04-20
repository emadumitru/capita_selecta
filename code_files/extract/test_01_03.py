import unittest
from unittest.mock import patch
import pre_01_03
import ref_01_03

class TestCpuMonitor(unittest.TestCase):
    @patch('pre_01_03.psutil.cpu_percent', return_value=10.0)
    @patch('builtins.print')
    def test_pre_cpu_monitor(self, mock_print, mock_cpu_percent):
        pre_01_03.monitor_cpu_usage()
        mock_print.assert_called_once_with('CPU Usage: 10.0%')

    @patch('ref_01_03.psutil.cpu_percent', return_value=10.0)
    @patch('builtins.print')
    def test_ref_cpu_monitor(self, mock_print, mock_cpu_percent):
        ref_01_03.monitor_cpu_usage()
        mock_print.assert_called_once_with('CPU Usage: 10.0%')

if __name__ == '__main__':
    unittest.main()