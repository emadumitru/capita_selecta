import random

def print_rolls(rolls):
    print("Dice Rolls:")
    for roll in rolls:
        print(f" - {roll}")

def main():
    num_rolls = 5
    rolls = []
    for _ in range(num_rolls):
        rolls.append(random.randint(1, 6))
    print_rolls(rolls)

if __name__ == "__main__":
    main()
