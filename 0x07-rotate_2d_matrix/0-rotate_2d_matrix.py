#!/usr/bin/python3
"""
Rotate 2D Matrix by 90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    # Transpose the matrix (swap rows with columns)
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reversing each row
    for i in range(n):
        matrix[i].reverse()
