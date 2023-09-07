# mostrar instalando numpy (.array, .transpose, .tolist)

"""
matrix[i][j] --> transp[j][i]
"""


def transpose(matrix):
    f = len(matrix)
    c = len(matrix[0])

    transposed_matrix = []
    for _ in range(c):
        transposed_matrix.append([0] * f)

    for i in range(f):
        for j in range(c):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

