#!/usr/bin/python3

"""
Rotate 2D matrix.
"""


def rotate_2d_matrix(matrix):
    """
    Function to rotate 2-d matrix.
    """
    if matrix is None:
        return

    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()
