import unittest
from pre_04_05 import roll_multiple_dice as pre_roll_multiple_dice
from ref_04_05 import roll_multiple_dice as ref_roll_multiple_dice

class TestDiceRoll(unittest.TestCase):
    def test_pre_roll_multiple_dice(self):
        num_dice = 2
        pre_rolls = pre_roll_multiple_dice(num_dice)
        self.assertEqual(len(pre_rolls), num_dice)
        for roll in pre_rolls:
            self.assertIn(roll, ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"])

    def test_ref_roll_multiple_dice(self):
        num_dice = 2
        ref_rolls = ref_roll_multiple_dice(num_dice)
        self.assertEqual(len(ref_rolls), num_dice)
        for roll in ref_rolls:
            self.assertIn(roll, ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"])

if __name__ == '__main__':
    unittest.main()
