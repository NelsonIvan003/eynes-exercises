# mostrar instalando numpy (.array, .transpose, .tolist)

"""
matrix[i][j] --> transp[j][i]
"""


def transpose(matrix):
    f = len(matrix)
    print(f)
    c = len(matrix[0])
    print(c)

    transposed_matrix = []
    for _ in range(c):
        transposed_matrix.append([0] * f)

    for i in range(f):
        for j in range(c):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

# Prueba con los ej del readme
input1 = [[1, 2]]
print(input1)
print(transpose(input1))

input2 = [[1, 2], [3, 4], [5, 6]]
print(input2)
print(transpose(input2))

input3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(input3)
print(transpose(input3))

