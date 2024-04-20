import unittest
import string
from pre_02_05 import generate_password as pre_generate_password
from ref_02_05 import generate_random_password as ref_generate_password

class TestPasswordGeneration(unittest.TestCase):
    def test_pre_generate_password(self):
        password_length = 12
        password = pre_generate_password(password_length)
        self.assertEqual(len(password), password_length)
        self.assertTrue(any(c.isalpha() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_ref_generate_password(self):
        password_length = 12
        password = ref_generate_password(password_length)
        self.assertEqual(len(password), password_length)
        self.assertTrue(any(c.isalpha() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

if __name__ == '__main__':
    unittest.main()
