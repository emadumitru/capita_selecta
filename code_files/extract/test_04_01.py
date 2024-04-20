import unittest
from pre_04_01 import roll_multiple_dice as pre_roll_multiple_dice
from ref_04_01 import roll_multiple_dice as ref_roll_multiple_dice

class TestDiceRolls(unittest.TestCase):
    def test_pre_roll_multiple_dice(self):
        num_dice = 5
        rolls = pre_roll_multiple_dice(num_dice)
        self.assertEqual(len(rolls), num_dice)
        for roll in rolls:
            self.assertGreaterEqual(roll, 1)
            self.assertLessEqual(roll, 6)

    def test_ref_roll_multiple_dice(self):
        num_dice = 5
        rolls = ref_roll_multiple_dice(num_dice)
        self.assertEqual(len(rolls), num_dice)
        for roll in rolls:
            self.assertGreaterEqual(roll, 1)
            self.assertLessEqual(roll, 6)

if __name__ == '__main__':
    unittest.main()
