import unittest
from pre_04_03 import dice_roller, print_rolls
from ref_04_03 import main as ref_main

class TestDiceRoller(unittest.TestCase):
    def test_dice_roller(self):
        num_rolls = 5
        pre_rolls = dice_roller(num_rolls)
        ref_main()
        self.assertEqual(pre_rolls, ref_main.rolls)

    def test_print_rolls(self):
        rolls = [1, 2, 3, 4, 5]
        expected_output = "Dice Rolls:\n - 1\n - 2\n - 3\n - 4\n - 5\n"
        self.assertEqual(expected_output, print_rolls(rolls))

if __name__ == '__main__':
    unittest.main()
