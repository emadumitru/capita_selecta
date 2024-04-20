import unittest
import string
from pre_02_02 import generate_password as pre_generate_password
from ref_02_02 import generate_password as ref_generate_password, generate_and_print_password

class TestPasswordGeneration(unittest.TestCase):
    def test_pre_generate_password(self):
        # Test the pre-refactored generate_password function
        length = 12
        password = pre_generate_password(length)
        self.assertEqual(len(password), length)
        self.assertTrue(any(char.isalpha() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_ref_generate_password(self):
        # Test the refactored generate_password function
        length = 12
        password = ref_generate_password(length)
        self.assertEqual(len(password), length)
        self.assertTrue(any(char.isalpha() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_generate_and_print_password(self):
        # Test the generate_and_print_password function
        length = 12
        generate_and_print_password(length)
        # No assertions needed, just checking that the function runs without errors

if __name__ == '__main__':
    unittest.main()
