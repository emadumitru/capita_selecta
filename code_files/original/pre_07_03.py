### Type: Checker Game --- Style: Simple

def initialize_board():
    board = []
    for i in range(8):
        row = []
        for j in range(8):
            if (i + j) % 2 == 0:
                row.append(" ")
            else:
                row.append("X")
        board.append(row)
    return board

def print_board(board):
    for row in board:
        print(" ".join(row))

def move_piece(board, start, end):
    x1, y1 = start
    x2, y2 = end
    board[x2][y2] = board[x1][y1]
    board[x1][y1] = " "

def is_valid_move(board, start, end):
    x1, y1 = start
    x2, y2 = end
    if board[x1][y1] == "X" and board[x2][y2] == " " and abs(x2 - x1) == 1 and abs(y2 - y1) == 1:
        return True
    return False

def play_game():
    board = initialize_board()
    print("Welcome to the Checker Game!")
    print("Here is the initial board:")
    print_board(board)
    print("Let's make a move!")
    start = (0, 1)
    end = (1, 0)
    if is_valid_move(board, start, end):
        move_piece(board, start, end)
        print("Move successful!")
    else:
        print("Invalid move!")
    print("Here is the updated board:")
    print_board(board)

play_game()