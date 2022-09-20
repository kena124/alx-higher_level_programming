#!/usr/bin/python3
""" A program to solve the N queens problem
"""
import sys


def check_conflict(board, current):
    """ Check if the current queen conflict with the existing queens
    """
    for i in range(current):
        # check for row conflict
        if (board[i] == board[current]):
            return False
        # check for diagonal conflict
        if (current - i == abs(board[current] - board[i])):
            return False
    return True


def n_queens(board, n):
    """ Enumerate all possible solution for the n queens problem"""
    i = 0
    board[0] = 0

    while True:
        if not check_conflict(board, i):
            if board[i] + 1 > n - 1:
                board[i] = -1
                i -= 1
        else:
            if i == n - 1:
                output = []
                for tuble in enumerate(board):
                    output.append(list(tuble))
                print(output)
                board[i] = -1
                i -= 1
            else:
                i += 1

        while board[i] + 1 > n - 1 and i > 0:
            board[i] = -1
            i -= 1
        if board[i] + 1 > n - 1 and i == 0:
            break
        board[i] += 1


def main():
    """ Parse user argument """
    argv = sys.argv

    if (len(argv) != 2):
        print("Usage: nqueens N")
        sys.exit(1)
    n = argv[1]

    try:
        n = int(n)
    except ValueError:
        print("N must be a number")
        sys.exit()

    if (n < 4):
        print("N must be at least 4")
        sys.exit(1)

    board = [-1 for _ in range(n)]
    n_queens(board, n)


if __name__ == "__main__":
    main()
