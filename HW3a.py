import math

def is_symmetric(matrix):
    """
    Check if a matrix is symmetric.

    Parameters:
        matrix (list of lists): The matrix to check.

    Returns:
        bool: True if the matrix is symmetric, False otherwise.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def is_positive_definite(matrix):
    """
    Check if a matrix is positive definite.

    Parameters:
        matrix (list of lists): The matrix to check.

    Returns:
        bool: True if the matrix is positive definite, False otherwise.
    """
    n = len(matrix)
    for i in range(n):
        if matrix[i][i] <= 0:
            return False
        for j in range(i+1, n):
            if matrix[j][i] != matrix[i][j]:
                return False
    return True

def cholesky_decomposition(matrix):
    """
    Perform Cholesky decomposition of a matrix.

    Parameters:
        matrix (list of lists): The matrix to decompose.

    Returns:
        list of lists: The lower triangular matrix L.
    """
    n = len(matrix)
    L = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i+1):
            if i == j:
                sum_val = sum(L[i][k] ** 2 for k in range(j))
                L[i][j] = math.sqrt(matrix[i][i] - sum_val)
            else:
                sum_val = sum(L[i][k] * L[j][k] for k in range(j))
                L[i][j] = (matrix[i][j] - sum_val) / L[j][j]
    return L

def cholesky_solve(A, b):
    """
    Solve the matrix equation Ax=b using Cholesky decomposition.

    Parameters:
        A (list of lists): The coefficient matrix.
        b (list): The constant vector.

    Returns:
        list: The solution vector x.
    """
    L = cholesky_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution(transpose(L), y)
    return x

def transpose(matrix):
    """
    Transpose a matrix.

    Parameters:
        matrix (list of lists): The matrix to transpose.

    Returns:
        list of lists: The transposed matrix.
    """
    n = len(matrix)
    return [[matrix[j][i] for j in range(n)] for i in range(n)]

def forward_substitution(L, b):
    """
    Perform forward substitution.

    Parameters:
        L (list of lists): Lower triangular matrix.
        b (list): The constant vector.

    Returns:
        list: The solution vector y.
    """
    n = len(L)
    y = [0.0] * n

    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]
        y[i] /= L[i][i]
    return y

def backward_substitution(U, b):
    """
    Perform backward substitution.

    Parameters:
        U (list of lists): Upper triangular matrix.
        b (list): The constant vector.

    Returns:
        list: The solution vector x.
    """
    n = len(U)
    x = [0.0] * n

    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]
    return x

def doolittle_decomposition(matrix):
    """
    Perform Doolittle decomposition of a matrix.

    Parameters:
        matrix (list of lists): The matrix to decompose.

    Returns:
        tuple: Lower triangular matrix L, upper triangular matrix U.
    """
    n = len(matrix)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for k in range(i, n):
            sum_val = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = matrix[i][k] - sum_val

        for k in range(i, n):
            if i == k:
                L[i][i] = 1.0
            else:
                sum_val = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (matrix[k][i] - sum_val) / U[i][i]
    return L, U

def doolittle_solve(A, b):
    """
    Solve the matrix equation Ax=b using Doolittle decomposition.

    Parameters:
        A (list of lists): The coefficient matrix.
        b (list): The constant vector.

    Returns:
        list: The solution vector x.
    """
    L, U = doolittle_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
    return x

def solve_matrix_equation(A, b):
    """
    Solve the matrix equation Ax=b using Cholesky decomposition if A is symmetric positive definite,
    otherwise use Doolittle decomposition.

    Parameters:
        A (list of lists): The coefficient matrix.
        b (list): The constant vector.

    Returns:
        list: The solution vector x.
    """
    if is_symmetric(A) and is_positive_definite(A):
        print("Symmetric positive definite matrix. Using Cholesky method.")
        return cholesky_solve(A, b)
    else:
        print("Not symmetric positive definite matrix. Using Doolittle method.")
        return doolittle_solve(A, b)

# Example problems
A1 = [[1, 1, 3, 2],
    [-1, 5, -5, -2],
    [3, -5, 19, 3],
    [2, -2, 3, 21]]

b1 = [15, -35, 94, 1]

A2 = [[4, 2, 4, 0],
      [2, 2, 3, 2],
      [4, 3, 6, 3],
      [0, 2, 3, 9]]

b2 = [20, 36, 60, 122]

print("Problem 1:")
solution1 = solve_matrix_equation(A1, b1)
print("Solution vector:")
print(solution1)

print("\nProblem 2:")
solution2 = solve_matrix_equation(A2, b2)
print("Solution vector:")
print(solution2)
