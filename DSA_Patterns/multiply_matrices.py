def multiply_matrices(a,b):
    row1=len(a)
    col1=len(a[0])

    row2=len(b)
    col2=len(b[0])

    if row2!=col1:
        return "Matrix multiplication is not possible"
    result=[[0 for _ in range(col2)] for _ in range(row1)]

    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                result[i][j] += a[i][k] * b[k][j]

    return result


matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

result_matrix = multiply_matrices(matrix1, matrix2)

print(result_matrix)