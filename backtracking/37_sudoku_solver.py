"""
--- Hard ---

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all the following rules:

- Each of the digits 1-9 must occur exactly once in each row.
- Each of the digits 1-9 must occur exactly once in each column.
- Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.
"""


def solve(board, r=0, c=0):
    if r == 9:
        return True

    elif c == 9:
        return solve(board, r + 1, 0)

    elif board[r][c] != ".":
        return solve(board, r, c + 1)

    else:
        for k in range(1, 10):
            if is_valid(board, r, c, str(k)):
                board[r][c] = str(k)

                if solve(board, r, c + 1):
                    return True

                board[r][c] = "."

        return False


def is_valid(board, row, col, value):
    not_in_row = value not in board[row]
    not_in_column = value not in [board[i][col] for i in range(9)]
    not_in_box = value not in [board[i][j] for i in range(row//3*3, row//3*3+3) for j in range(col//3*3, col//3*3+3)]

    return not_in_row and not_in_column and not_in_box


solve([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
