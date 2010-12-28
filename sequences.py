import math


def generate_fibonacci():
    pass 

def zero_matrix(m, n):
    return [[0 for row in range(n)] for col in range(m)]

def matrix_mul(matrix1, matrix2, mod=None):
    if len(matrix1[0]) != len(matrix2[0]):
        raise Exception("Matrices dimension must be m*n and n*p to multiple")    
    new_matrix = zero_matrix(len(matrix1), len(matrix2[0]))
    # multiply if dimension is correct 
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                new_matrix[i][j] += matrix1[i][k]*matrix2[k][j]
            # optional modulus  
            if mod is not None:
                new_matrix[i][j] = new_matrix[i][j] % mod 

    return new_matrix


def fibonacci_matrix(n, mod=None):
    """
    Calculate large fib value using matrix form in log(n) steps
    """
    def matrix_mul2(m1, m2):
        return matrix_mul(m1, m2, mod)
        
    b = [int(d) for d in bin(n)[2:]]
    b.reverse()
    p = zip(b, range(len(b)))
    m = { 0: [[1,1],[1,0]] }
    for i in range(1, len(b)):
        m[i] = matrix_mul2(m[i-1], m[i-1])
    ms = [m[y] for (x,y) in p if x == 1]
    return reduce(matrix_mul2, ms)[0][1]
