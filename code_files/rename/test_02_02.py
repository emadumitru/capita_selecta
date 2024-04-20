import unittest
import string
from pre_02_02 import generate_password as pre_generate_password
from ref_02_02 import generate_secure_password as ref_generate_secure_password

class TestPasswordGeneration(unittest.TestCase):
    def test_pre_generate_password(self):
        # Test the functionality of pre_generate_password
        length = 12
        password = pre_generate_password(length)
        self.assertEqual(len(password), length)
        self.assertTrue(any(char.isalpha() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_ref_generate_secure_password(self):
        # Test the functionality of ref_generate_secure_password
        length = 12
        password = ref_generate_secure_password(length)
        self.assertEqual(len(password), length)
        self.assertTrue(any(char.isalpha() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

if __name__ == '__main__':
    unittest.main()
