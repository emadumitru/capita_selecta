def initialize_board():
    board = []
    for row in range(8):
        board.append([])
        for col in range(8):
            if (row + col) % 2 == 0:
                board[row].append(" ")
            else:
                board[row].append("X")
    return board

def print_board(board):
    print("  A B C D E F G H")
    for row in range(8):
        print(row + 1, end=" ")
        for col in range(8):
            print(board[row][col], end=" ")
        print()

def move_piece(board, start, end):
    start_row, start_col = start
    end_row, end_col = end
    board[end_row][end_col] = board[start_row][start_col]
    board[start_row][start_col] = " "

def is_valid_move(board, start, end):
    start_row, start_col = start
    end_row, end_col = end
    if board[start_row][start_col] == " ":
        return False
    if board[end_row][end_col] != " ":
        return False
    if abs(start_row - end_row) != 1 or abs(start_col - end_col) != 1:
        return False
    return True

def play_game():
    board = initialize_board()
    print("Welcome to the Peaceful Checker Game!")
    print("You can move your piece diagonally to an empty space.")
    print("The goal is to reach the opposite side of the board.")
    print("Let's start!")
    print_board(board)
    while True:
        start = (int(input("Enter the row of the piece you want to move: ")) - 1,
                 ord(input("Enter the column of the piece you want to move: ").upper()) - ord("A"))
        end = (int(input("Enter the row where you want to move the piece: ")) - 1,
               ord(input("Enter the column where you want to move the piece: ").upper()) - ord("A"))
        if is_valid_move(board, start, end):
            move_piece(board, start, end)
            print_board(board)
            if end[0] == 0:
                print("Congratulations! You reached the opposite side of the board.")
                break
        else:
            print("Invalid move. Please try again.")

play_game()