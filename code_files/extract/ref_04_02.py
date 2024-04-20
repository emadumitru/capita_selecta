import random

def roll_dice():
    dice = [
        " _________ ",
        "|         |",
        "|    *    |",
        "|         |",
        " ‾‾‾‾‾‾‾‾‾ "
    ]
    
    dice_faces = {
        1: [dice[0], dice[1], dice[2], dice[3], dice[4]],
        2: [dice[0], dice[1], dice[2], dice[3], dice[1]],
        3: [dice[0], dice[1], dice[2], dice[3], dice[2]],
        4: [dice[0], dice[1], dice[2], dice[3], dice[3]],
        5: [dice[0], dice[1], dice[2], dice[3], dice[2]],
        6: [dice[0], dice[1], dice[2], dice[3], dice[4]]
    }
    
    roll = random.randint(1, 6)
    
    for line in dice_faces[roll]:
        print(line)

def main():
    roll_dice()

if __name__ == "__main__":
    main()