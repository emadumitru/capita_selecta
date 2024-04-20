### Type: Checker Game --- Style: Modular

# Checker Game

def initialize_board():
    board = []
    for row in range(8):
        board.append([])
        for col in range(8):
            if row < 3 and (row + col) % 2 == 0:
                board[row].append('X')
            elif row > 4 and (row + col) % 2 == 0:
                board[row].append('O')
            else:
                board[row].append(' ')
    return board

def print_board(board):
    print("   0  1  2  3  4  5  6  7")
    for row in range(8):
        print(row, end=" ")
        for col in range(8):
            print(f"[{board[row][col]}]", end=" ")
        print()

def main():
    board = initialize_board()
    print_board(board)

if __name__ == "__main__":
    main()