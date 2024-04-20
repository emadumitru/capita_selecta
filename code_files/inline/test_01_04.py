import unittest
from unittest.mock import patch
import pre_01_04
import ref_01_04

class TestMonitorCpuUsage(unittest.TestCase):
    @patch('pre_01_04.psutil.cpu_percent')
    @patch('pre_01_04.print')
    def test_pre_monitor_cpu_usage(self, mock_print, mock_cpu_percent):
        mock_cpu_percent.return_value = 10.5
        with self.assertRaises(StopIteration):
            pre_01_04.monitor_cpu_usage()
        mock_print.assert_called_once_with('Current CPU Usage: 10.5%')

    @patch('ref_01_04.psutil.cpu_percent')
    @patch('ref_01_04.print')
    def test_ref_monitor_cpu_usage(self, mock_print, mock_cpu_percent):
        mock_cpu_percent.return_value = 10.5
        with self.assertRaises(StopIteration):
            ref_01_04.monitor_cpu_usage()
        mock_print.assert_called_once_with('Current CPU Usage: 10.5%')

if __name__ == '__main__':
    unittest.main()