import unittest
from pre_04_04 import roll_dice
from ref_04_04 import roll_and_sum_dice

class TestDiceRoller(unittest.TestCase):
    def test_roll_dice(self):
        # Test roll_dice function from pre_04_04.py
        num_dice = 2
        num_sides = 6
        result = roll_dice(num_dice, num_sides)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, num_dice)
        self.assertLessEqual(result, num_dice * num_sides)

    def test_roll_and_sum_dice(self):
        # Test roll_and_sum_dice function from ref_04_04.py
        num_dice = 2
        num_sides = 6
        result = roll_and_sum_dice(num_dice, num_sides)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, num_dice)
        self.assertLessEqual(result, num_dice * num_sides)

if __name__ == '__main__':
    unittest.main()
