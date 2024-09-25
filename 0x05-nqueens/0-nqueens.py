#!/usr/bin/python3
"""
This module solves the N Queens problem.

The N Queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard. This program finds all possible solutions for
a given N >= 4 and prints them in a readable format.
"""
import sys


def is_safe(board, row, col):
    """_summary_

    Args:
        board (_type_): _description_
        row (_type_): _description_
        col (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col):
    """_summary_

    Args:
        board (_type_): _description_
        col (_type_): _description_

    Returns:
        _type_: _description_
    """
    if col >= len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return True

    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1) or res
            board[i][col] = 0  # Backtrack

    return res


def solve_nqueens(N):
    """_summary_

    Args:
        N (_type_): _description_
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens_util(board, 0)


def main():
    """_summary_
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)


if __name__ == "__main__":
    main()
