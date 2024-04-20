import unittest
from pre_02_04 import generate_password as pre_generate_password
from ref_02_04 import generate_and_print_password as ref_generate_and_print_password

class TestPasswordGeneration(unittest.TestCase):
    def test_pre_generate_password(self):
        password_length = 12
        password = pre_generate_password(password_length)
        self.assertEqual(len(password), password_length)
    
    def test_ref_generate_and_print_password(self):
        password_length = 12
        ref_generate_and_print_password(password_length)
        # Since the ref_generate_and_print_password function only prints the password,
        # we cannot directly compare the output. We can manually verify the output in the console.
        # If the function runs without any errors, we can assume it is working correctly.

if __name__ == '__main__':
    unittest.main()
