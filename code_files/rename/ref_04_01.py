import random

def generate_random_number():
    return random.randint(1, 6)

def roll_multiple_dice(num_dice):
    rolls = []
    for _ in range(num_dice):
        rolls.append(generate_random_number())
    return rolls

def display_rolls(rolls):
    print("Dice Rolls:")
    for roll in rolls:
        print(f" - {roll}")

def main():
    num_dice = 5
    rolls = roll_multiple_dice(num_dice)
    display_rolls(rolls)

if __name__ == "__main__":
    main()
