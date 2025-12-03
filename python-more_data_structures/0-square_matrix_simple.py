#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for i in matrix:
        inside_matrix = []
        for j in i:
            inside_matrix.append(j**2)
        new_matrix.append(inside_matrix)
    return new_matrix
