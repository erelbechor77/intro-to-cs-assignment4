
def is_valid(board, row, col, num):
    # Check if 'num' is not in the given row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check if 'num' is not in the given column
    for x in range(9):
        if board[x][col] == num:
            return False
    # Check if 'num' is not in the 3x3 sub-grid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False    
    return True
def solve_sudoku(board):
    empty = find_empty_location(board)
    if not empty:
        return True  # Puzzle solved
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # Backtrack
    return False
def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

