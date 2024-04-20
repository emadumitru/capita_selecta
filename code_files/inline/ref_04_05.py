import random

def roll_multiple_dice(num_dice):
    dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    rolls = []
    print("Rolling the dice...")
    for _ in range(num_dice):
        roll = random.choice(dice_faces)
        rolls.append(roll)
        print(roll, end=" ")
    print()
    return rolls

def main():
    num_dice = 2
    rolls = roll_multiple_dice(num_dice)

if __name__ == "__main__":
    main()
