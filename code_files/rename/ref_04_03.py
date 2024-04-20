import random

def roll_dice():
    return random.randint(1, 6)

def generate_dice_rolls(num_rolls):
    rolls = []
    for _ in range(num_rolls):
        rolls.append(roll_dice())
    return rolls

def print_rolls(rolls):
    print("Dice Rolls:")
    for roll in rolls:
        print(f" - {roll}")

def main():
    num_rolls = 5
    rolls = generate_dice_rolls(num_rolls)
    print_rolls(rolls)

if __name__ == "__main__":
    main()
