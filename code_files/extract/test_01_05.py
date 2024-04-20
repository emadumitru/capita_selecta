import unittest
from pre_01_05 import monitor_cpu_usage as pre_monitor_cpu_usage
from ref_01_05 import monitor_cpu_usage as ref_monitor_cpu_usage

class TestCPUUsage(unittest.TestCase):
    def test_pre_refactored_code(self):
        # Test the pre-refactored code
        # Mock the print function to capture the output
        import builtins
        from io import StringIO

        # Create a StringIO object to capture the output
        output = StringIO()
        builtins.print = lambda *args, **kwargs: output.write(" ".join(map(str, args)) + "\n")

        # Call the function
        pre_monitor_cpu_usage()

        # Get the captured output
        output_value = output.getvalue()

        # Assert that the output contains the expected string
        self.assertIn("Current CPU Usage:", output_value)

    def test_refactored_code(self):
        # Test the refactored code
        # Mock the print function to capture the output
        import builtins
        from io import StringIO

        # Create a StringIO object to capture the output
        output = StringIO()
        builtins.print = lambda *args, **kwargs: output.write(" ".join(map(str, args)) + "\n")

        # Call the function
        ref_monitor_cpu_usage()

        # Get the captured output
        output_value = output.getvalue()

        # Assert that the output contains the expected string
        self.assertIn("Current CPU Usage:", output_value)

if __name__ == '__main__':
    unittest.main()
