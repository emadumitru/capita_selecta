import unittest
from pre_04_03 import dice_roller as pre_dice_roller
from ref_04_03 import dice_roller as ref_dice_roller

class TestDiceRoller(unittest.TestCase):
    def test_pre_dice_roller(self):
        num_rolls = 5
        rolls = pre_dice_roller(num_rolls)
        self.assertEqual(len(rolls), num_rolls)
        self.assertTrue(all(1 <= roll <= 6 for roll in rolls))

    def test_ref_dice_roller(self):
        num_rolls = 5
        rolls = ref_dice_roller(num_rolls)
        self.assertEqual(len(rolls), num_rolls)
        self.assertTrue(all(1 <= roll <= 6 for roll in rolls))

if __name__ == '__main__':
    unittest.main()
