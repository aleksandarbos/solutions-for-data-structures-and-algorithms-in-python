"""R-5.12 Describe how the built-in sum function can be combined with Python’s
comprehension syntax to compute the sum of all numbers in an n×n data
set, represented as a list of lists."""

A = [[1,2,3], [4,5,6], [7,8,9]]

def sum_matrix(matrix):
    return sum([sum(matrix[i]) for i in range(len(matrix))])


print(sum_matrix(A))
