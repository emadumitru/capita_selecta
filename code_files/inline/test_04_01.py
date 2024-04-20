import unittest
import io
from pre_04_01 import roll_multiple_dice, display_rolls
from ref_04_01 import main as ref_main

class TestDiceRolls(unittest.TestCase):
    def test_roll_multiple_dice(self):
        num_dice = 5
        rolls = roll_multiple_dice(num_dice)
        self.assertEqual(len(rolls), num_dice)
        for roll in rolls:
            self.assertGreaterEqual(roll, 1)
            self.assertLessEqual(roll, 6)

    def test_display_rolls(self):
        rolls = [1, 2, 3, 4, 5]
        expected_output = "Dice Rolls:\n - 1\n - 2\n - 3\n - 4\n - 5\n"
        stdout = io.StringIO()
        with unittest.mock.patch('sys.stdout', stdout):
            display_rolls(rolls)
        self.assertEqual(stdout.getvalue(), expected_output)

    def test_main(self):
        expected_output = "Dice Rolls:\n - 1\n - 2\n - 3\n - 4\n - 5\n"
        stdout = io.StringIO()
        with unittest.mock.patch('sys.stdout', stdout):
            ref_main()
        self.assertEqual(stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
