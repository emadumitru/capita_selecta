import unittest
from pre_02_05 import generate_password as pre_generate_password
from ref_02_05 import generate_password as ref_generate_password, generate_and_print_password

class TestPasswordGenerator(unittest.TestCase):
    def test_generate_password(self):
        pre_password = pre_generate_password(12)
        ref_password = ref_generate_password(12)
        self.assertEqual(len(pre_password), 12)
        self.assertEqual(len(ref_password), 12)
        self.assertNotEqual(pre_password, ref_password)

    def test_generate_and_print_password(self):
        # Redirect stdout to capture the print output
        import sys
        from io import StringIO
        captured_output = StringIO()
        sys.stdout = captured_output

        generate_and_print_password(12)

        sys.stdout = sys.__stdout__  # Reset stdout
        output = captured_output.getvalue().strip()
        self.assertTrue(output.startswith("Generated Password:"))

if __name__ == '__main__':
    unittest.main()
