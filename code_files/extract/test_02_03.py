import unittest
import io
import sys
from pre_02_03 import generate_password as pre_generate_password
from ref_02_03 import generate_password as ref_generate_password
from ref_02_03 import print_generated_password

class TestPasswordGeneration(unittest.TestCase):
    def test_pre_generate_password(self):
        password_length = 12
        password = pre_generate_password(password_length)
        self.assertEqual(len(password), password_length)

    def test_ref_generate_password(self):
        password_length = 12
        password = ref_generate_password(password_length)
        self.assertEqual(len(password), password_length)

    def test_print_generated_password(self):
        password = "TestPassword123!"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_generated_password(password)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Generated Password: TestPassword123!")

if __name__ == '__main__':
    unittest.main()
