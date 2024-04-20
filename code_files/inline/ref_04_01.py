import random

def main():
    num_dice = 5
    rolls = []
    for _ in range(num_dice):
        rolls.append(random.randint(1, 6))
    print("Dice Rolls:")
    for roll in rolls:
        print(f" - {roll}")

if __name__ == "__main__":
    main()
