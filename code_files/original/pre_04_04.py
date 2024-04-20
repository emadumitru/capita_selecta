### Type: Dice Roller --- Style: Modular

import random

def roll_dice(num_dice, num_sides):
    """
    Roll the dice and return the total sum of the rolls.
    """
    total = 0
    for _ in range(num_dice):
        roll = random.randint(1, num_sides)
        total += roll
    return total

def main():
    """
    Main function to run the dice roller program.
    """
    num_dice = 2
    num_sides = 6
    total = roll_dice(num_dice, num_sides)
    print(f"Total roll: {total}")

if __name__ == "__main__":
    main()