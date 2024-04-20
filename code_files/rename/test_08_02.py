import unittest
from pre_08_02 import generate_color_code, convert_to_rgb, convert_to_hex
from ref_08_02 import generate_random_color_code

class TestColorConversion(unittest.TestCase):
    def test_generate_color_code(self):
        color_code = generate_color_code()
        self.assertEqual(len(color_code), 6)
        self.assertTrue(all(c in "0123456789ABCDEF" for c in color_code))

    def test_generate_random_color_code(self):
        color_code = generate_random_color_code()
        self.assertEqual(len(color_code), 6)
        self.assertTrue(all(c in "0123456789ABCDEF" for c in color_code))

    def test_convert_to_rgb(self):
        color_code = generate_color_code()
        rgb = convert_to_rgb(color_code)
        self.assertIsInstance(rgb, tuple)
        self.assertEqual(len(rgb), 3)
        self.assertTrue(all(isinstance(c, int) for c in rgb))
        self.assertTrue(all(0 <= c <= 255 for c in rgb))

    def test_convert_to_hex(self):
        rgb = (255, 0, 128)
        converted_color_code = convert_to_hex(rgb)
        self.assertEqual(len(converted_color_code), 6)
        self.assertTrue(all(c in "0123456789ABCDEF" for c in converted_color_code))

if __name__ == '__main__':
    unittest.main()
