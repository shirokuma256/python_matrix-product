import sys
import numpy as np
from datetime import datetime
from memory_profiler import profile

@profile
def matrix_product(n):
    # create two matrices of size (n, n) with random elements
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)

    # initialize an empty matrix of size (n, n)
    C = np.zeros((n, n))

    # perform matrix multiplication using for loops
    start_time = datetime.now()
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    end_time = datetime.now()
    elapsed_time = end_time - start_time

    # print the result and elapsed time
    print("Result matrix:")
    print(C)
    print("Elapsed time: ", elapsed_time)

if __name__ == '__main__':
    # check if the argument is provided
    if len(sys.argv) < 2:
        print("Error: Missing argument n")
        sys.exit(1)

    # parse the argument as integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: Invalid argument n")
        sys.exit(1)

    # calculate matrix product
    matrix_product(n)
