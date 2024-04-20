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
    print("   A B C D E F G H")
    print("  -----------------")
    for i in range(8):
        print(i + 1, "|", end="")
        for j in range(8):
            print(board[i][j], end=" ")
        print("|", i + 1)
    print("  -----------------")
    print("   A B C D E F G H")

def make_move(board, start, end):
    start_row, start_col = start
    end_row, end_col = end
    piece = board[start_row][start_col]
    board[start_row][start_col] = " "
    board[end_row][end_col] = piece

def is_valid_move(board, start, end):
    start_row, start_col = start
    end_row, end_col = end
    piece = board[start_row][start_col]
    if piece == " ":
        return False
    if end_row < 0 or end_row > 7 or end_col < 0 or end_col > 7:
        return False
    if board[end_row][end_col] != " ":
        return False
    if abs(end_row - start_row) != abs(end_col - start_col):
        return False
    return True

def main():
    board = initialize_board()
    print_board(board)
    start = (1, 0)
    end = (2, 1)
    if is_valid_move(board, start, end):
        make_move(board, start, end)
    print_board(board)

if __name__ == "__main__":
    main()