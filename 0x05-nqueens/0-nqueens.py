#!/usr/bin/env python3
"""
This module solves the N Queens problem.

The N Queens puzzle is the challenge of placing N non-attacking queens
on an N×N chessboard. This program finds all possible solutions for
a given N >= 4 and prints them in a readable format.
"""

import sys
from typing import List, Tuple


def is_safe(board: List[int], row: int, col: int) -> bool:
    """
    Check if it's safe to place a queen at the given position.

    Args:
        board (List[int]): Current state of the board.
        row (int): Row to check.
        col (int): Column to check.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(n: int) -> List[List[Tuple[int, int]]]:
    """
    Solve the N Queens problem and return all solutions.

    Args:
        n (int): Size of the chessboard and number of queens.

    Returns:
        List[List[Tuple[int, int]]]: List of all solutions, where each solution
        is represented as a list of (row, col) tuples.
    """
    def backtrack(row: int) -> None:
        if row == n:
            solutions.append([(i, board[i]) for i in range(n)])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                # Reset the row position to allow for other possibilities
                board[row] = -1

    board = [-1] * n
    solutions = []
    backtrack(0)
    return solutions


def print_solutions(solutions: List[List[Tuple[int, int]]], n: int) -> None:
    """
    Print all solutions in a readable chessboard format.

    Args:
        solutions (List[List[Tuple[int, int]]]):
        List of all solutions to be printed.
        n (int): Size of the chessboard.
    """
    for solution in solutions:
        print("Solution:")
        for row, col in solution:
            line = ['.'] * n
            line[col] = 'Q'
            print(" ".join(line))
        print()  # Add a blank line between solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    print_solutions(solutions, n)
