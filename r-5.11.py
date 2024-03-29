"""
R-5.11 Use standard control structures to compute the sum of all numbers in an
n×n data set, represented as a list of lists.
"""


def matrix_sum(matrix):
    s = 0
    for i in range(0, len(matrix)):
        for j in range(len(matrix[i])):
            s += matrix[i][j]
    return s

if __name__ == "__main__":
    A = [[1,2,3], [4,5,6], [7,8,9]]
    assert matrix_sum(A) == 45
