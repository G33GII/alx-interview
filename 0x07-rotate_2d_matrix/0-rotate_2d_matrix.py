#!/usr/bin/python3
""" Rotate 2D Matrix
This script contains a function to rotate a given n x n 2D matrix
90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the input 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): A square matrix to be rotated.

    Returns:
        None: The function modifies the input matrix directly.
    """
    # Iterate over the indices of the matrix
    for row_index, column_values in enumerate(zip(*reversed(matrix))):
        # Assign the rotated values back to the original matrix
        matrix[row_index] = list(column_values)


if __name__ == '__main__':
    # Define a sample 3x3 matrix
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    # Call the rotate function to rotate the matrix
    rotate_2d_matrix(matrix)

    # Print the rotated matrix
    print(matrix)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
