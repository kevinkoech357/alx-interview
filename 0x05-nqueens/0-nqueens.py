#!/usr/bin/python3

"""
Solve N queens puzzle.
"""


import sys


def is_safe(col, row, board):
    """
    Checks if placing a queen at (row, col) is safe (no attacks).
    """
    # Check row and diagonal attacks
    for c, r in enumerate(board):
        if r == row or abs(c - col) == abs(r - row):
            return False
    return True


def solve_n_queens(n, col, board=[], solutions=[]):
    """
    Solves the N queens problem using backtracking.
    """
    if col == n:
        solutions.append([i for i in board])
        return

    for row in range(n):
        if is_safe(col, row, board):
            solve_n_queens(n, col + 1, board + [row], solutions)

    return solutions


def main():
    """
    Check if cli arg passes set requirements.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)

    if n < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)

    solutions = solve_n_queens(n, 0)
    if not solutions:
        print("No solutions found")
    else:
        for solution in solutions:
            print([[row, solution[row]] for row in range(len(solution))])


if __name__ == "__main__":
    main()
