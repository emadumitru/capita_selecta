import unittest
from pre_04_03 import dice_roller as pre_dice_roller
from ref_04_03 import generate_dice_rolls as ref_generate_dice_rolls

class TestDiceRoller(unittest.TestCase):
    def test_dice_roller(self):
        num_rolls = 5

        # Test the pre-refactored code
        pre_rolls = pre_dice_roller(num_rolls)
        self.assertEqual(len(pre_rolls), num_rolls)
        self.assertTrue(all(1 <= roll <= 6 for roll in pre_rolls))

        # Test the refactored code
        ref_rolls = ref_generate_dice_rolls(num_rolls)
        self.assertEqual(len(ref_rolls), num_rolls)
        self.assertTrue(all(1 <= roll <= 6 for roll in ref_rolls))

if __name__ == '__main__':
    unittest.main()
