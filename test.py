def matrix_multiply(a, b):
    """
    Multiplies two matrices together and returns the result.
    Assumes that the matrices are compatible for multiplication.
    """
    # Get the dimensions of the matrices
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])

    # Create a new matrix to hold the result
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    # Perform the multiplication
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]

    return result
