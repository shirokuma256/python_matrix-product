
# -*- coding: utf-8 -*-
import sys
from memory_profiler import profile
import csv
@profile

def matrix_product(n):
    import numpy as np
    a = np.random.rand(n, n)
    b = np.random.rand(n, n)
    c = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i, j] += a[i, k] * b[k, j]
    return c

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: python3 matrix_product.py [N]')
        sys.exit(1)

    n = int(sys.argv[1])
    result = matrix_product(n)
    
    with open('memory_profile.csv', mode='w') as file:
        writer = csv.writer(file)
        writer.writerows(result)
