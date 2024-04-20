import random

def roll_dice():
    dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    return random.choice(dice_faces)

def roll_multiple_dice(num_dice):
    rolls = []
    for _ in range(num_dice):
        rolls.append(roll_dice())
    return rolls

def display_rolls(rolls):
    print("Rolling the dice...")
    for roll in rolls:
        print(roll, end=" ")
    print()

def main():
    num_dice = 2
    rolls = roll_multiple_dice(num_dice)
    display_rolls(rolls)

if __name__ == "__main__":
    main()