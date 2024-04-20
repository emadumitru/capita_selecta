import unittest
from pre_04_02 import roll_dice as pre_roll_dice
from ref_04_02 import roll_dice as ref_roll_dice

class TestDiceRoll(unittest.TestCase):
    def test_pre_roll_dice(self):
        # Test the pre-refactored roll_dice function
        # by checking if it prints the correct dice face
        # for each possible roll value
        for _ in range(10):
            pre_roll_dice()

    def test_ref_roll_dice(self):
        # Test the refactored roll_dice function
        # by checking if it prints the correct dice face
        # for each possible roll value
        for _ in range(10):
            ref_roll_dice()

if __name__ == '__main__':
    unittest.main()
