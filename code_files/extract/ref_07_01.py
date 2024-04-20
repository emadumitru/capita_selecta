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
    if x2 < 0 or x2 >= 8 or y2 < 0 or y2 >= 8:
        return False
    if board[x2][y2] != " ":
        return False
    if abs(x2 - x1) != abs(y2 - y1):
        return False
    return True

def play_checker_game():
    board = initialize_board()
    print("Welcome to the Checker Game!")
    print("Here is the initial board:")
    print_board(board)
    start = (2, 1)
    end = (3, 0)
    if is_valid_move(board, start, end):
        move_piece(board, start, end)
        print("Piece moved successfully!")
    else:
        print("Invalid move!")
    print("Here is the updated board:")
    print_board(board)

play_checker_game()