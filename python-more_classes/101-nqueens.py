#!/usr/bin/python3
"""This module solves the N queens puzzle with backtracking."""
import sys


def solve(n, row, cols, solution, results):
    """Place a queen on each row, keeping only safe positions.

    Args:
        n (int): the size of the board.
        row (int): the row being filled.
        cols (list): the column chosen for each earlier row.
        solution (list): the [row, column] pairs placed so far.
        results (list): every complete solution found.
    """
    if row == n:
        results.append([pos[:] for pos in solution])
        return
    for col in range(n):
        safe = True
        for r, c in enumerate(cols):
            if c == col or abs(c - col) == row - r:
                safe = False
                break
        if safe:
            cols.append(col)
            solution.append([row, col])
            solve(n, row + 1, cols, solution, results)
            cols.pop()
            solution.pop()


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
    results = []
    solve(n, 0, [], [], results)
    for result in results:
        print(result)
