import random

def roll_dice():
    dice_faces = {
        1: [
            " _________ ",
            "|         |",
            "|    *    |",
            "|         |",
            " ‾‾‾‾‾‾‾‾‾ "
        ],
        2: [
            " _________ ",
            "|         |",
            "|    *    |",
            "|         |",
            "|    *    |",
            " ‾‾‾‾‾‾‾‾‾ "
        ],
        3: [
            " _________ ",
            "|         |",
            "|    *    |",
            "|         |",
            "|  *  *  |",
            " ‾‾‾‾‾‾‾‾‾ "
        ],
        4: [
            " _________ ",
            "|         |",
            "|  *   *  |",
            "|         |",
            "|  *   *  |",
            " ‾‾‾‾‾‾‾‾‾ "
        ],
        5: [
            " _________ ",
            "|         |",
            "|  *   *  |",
            "|    *    |",
            "|  *   *  |",
            " ‾‾‾‾‾‾‾‾‾ "
        ],
        6: [
            " _________ ",
            "|         |",
            "|  *   *  |",
            "|  *   *  |",
            "|  *   *  |",
            " ‾‾‾‾‾‾‾‾‾ "
        ]
    }

    roll = random.randint(1, 6)

    for line in dice_faces[roll]:
        print(line)

roll_dice()