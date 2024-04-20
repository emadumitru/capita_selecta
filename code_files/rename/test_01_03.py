import unittest
import pre_01_03
import ref_01_03

class TestCPUUsage(unittest.TestCase):
    def test_cpu_usage(self):
        # Test the functionality of pre-refactored code
        pre_output = []
        pre_01_03.print = lambda x: pre_output.append(x)  # Redirect print statements to a list
        pre_01_03.monitor_cpu_usage()
        
        # Test the functionality of refactored code
        ref_output = []
        ref_01_03.print = lambda x: ref_output.append(x)  # Redirect print statements to a list
        ref_01_03.track_cpu_usage()
        
        # Verify that the outputs are the same
        self.assertEqual(pre_output, ref_output)

if __name__ == '__main__':
    unittest.main()
