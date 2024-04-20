import unittest
from pre_04_04 import roll_dice as pre_roll_dice
from ref_04_04 import roll_dice as ref_roll_dice

class TestDiceRoller(unittest.TestCase):
    def test_pre_roll_dice(self):
        self.assertEqual(pre_roll_dice(2, 6), ref_roll_dice(2, 6))
        self.assertEqual(pre_roll_dice(3, 4), ref_roll_dice(3, 4))
        self.assertEqual(pre_roll_dice(1, 10), ref_roll_dice(1, 10))
    
    def test_ref_roll_dice(self):
        self.assertEqual(ref_roll_dice(2, 6), pre_roll_dice(2, 6))
        self.assertEqual(ref_roll_dice(3, 4), pre_roll_dice(3, 4))
        self.assertEqual(ref_roll_dice(1, 10), pre_roll_dice(1, 10))

if __name__ == '__main__':
    unittest.main()
