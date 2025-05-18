#!/usr/bin/python3
def matrix_divided(matrix, div):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            num = round(matrix[i][j] / div)
            matrix_divided.append(num)
            try:    
                if matrix is not isinstance(matrix, str):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                elif len(matrix[0]) != len(matrix[1]):
                    raise TypeError("Each row of the matrix must have the same size")
                elif div is not isinstance(div, str):
                    raise TypeError("div must be a number")
                elif div != 0:
                    print("division by zero")
                else:
                    return matrix_divided
            except ZeroDivisionError:
                print("division by zero")
    return matrix_divided
