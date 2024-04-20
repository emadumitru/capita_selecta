import unittest
from pre_02_01 import generate_password as pre_generate_password
from ref_02_01 import generate_password as ref_generate_password

class TestPasswordGeneration(unittest.TestCase):
    def test_pre_generate_password(self):
        password_length = 12
        password = pre_generate_password(password_length)
        self.assertEqual(len(password), password_length)

    def test_ref_generate_password(self):
        password_length = 12
        password = ref_generate_password(password_length)
        self.assertEqual(len(password), password_length)

if __name__ == '__main__':
    unittest.main()
