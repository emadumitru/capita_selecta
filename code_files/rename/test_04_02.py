import unittest
from pre_04_02 import roll_dice
from ref_04_02 import display_dice

class TestDiceRoll(unittest.TestCase):
    def test_roll_dice(self):
        # Test the roll_dice function
        # Generate 100 rolls and check if the output is within the expected range
        for _ in range(100):
            roll_dice()
    
    def test_display_dice(self):
        # Test the display_dice function
        # Generate 100 rolls and check if the output is within the expected range
        for _ in range(100):
            display_dice()

if __name__ == '__main__':
    unittest.main()
