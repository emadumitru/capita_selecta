import unittest
from pre_04_04 import roll_dice as pre_roll_dice
from ref_04_04 import roll_dice as ref_roll_dice

class TestDiceRoller(unittest.TestCase):
    def test_pre_roll_dice(self):
        # Test with 2 dice and 6 sides
        num_dice = 2
        num_sides = 6
        pre_result = pre_roll_dice(num_dice, num_sides)
        self.assertIsInstance(pre_result, int)
        self.assertGreaterEqual(pre_result, num_dice)
        self.assertLessEqual(pre_result, num_dice * num_sides)

        # Test with 3 dice and 10 sides
        num_dice = 3
        num_sides = 10
        pre_result = pre_roll_dice(num_dice, num_sides)
        self.assertIsInstance(pre_result, int)
        self.assertGreaterEqual(pre_result, num_dice)
        self.assertLessEqual(pre_result, num_dice * num_sides)

    def test_ref_roll_dice(self):
        # Test with 2 dice and 6 sides
        num_dice = 2
        num_sides = 6
        ref_result = ref_roll_dice(num_dice, num_sides)
        self.assertIsInstance(ref_result, int)
        self.assertGreaterEqual(ref_result, num_dice)
        self.assertLessEqual(ref_result, num_dice * num_sides)

        # Test with 3 dice and 10 sides
        num_dice = 3
        num_sides = 10
        ref_result = ref_roll_dice(num_dice, num_sides)
        self.assertIsInstance(ref_result, int)
        self.assertGreaterEqual(ref_result, num_dice)
        self.assertLessEqual(ref_result, num_dice * num_sides)

if __name__ == '__main__':
    unittest.main()
