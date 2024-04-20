import unittest
from pre_04_05 import roll_multiple_dice as pre_roll_multiple_dice
from ref_04_05 import roll_multiple_dice as ref_roll_multiple_dice

class TestDiceRoll(unittest.TestCase):
    def test_pre_roll_multiple_dice(self):
        num_dice = 2
        pre_rolls = pre_roll_multiple_dice(num_dice)
        self.assertEqual(len(pre_rolls), num_dice)
        self.assertTrue(all(isinstance(roll, str) for roll in pre_rolls))

    def test_ref_roll_multiple_dice(self):
        num_dice = 2
        ref_rolls = ref_roll_multiple_dice(num_dice)
        self.assertEqual(len(ref_rolls), num_dice)
        self.assertTrue(all(isinstance(roll, str) for roll in ref_rolls))

if __name__ == '__main__':
    unittest.main()
