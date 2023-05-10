# -*- coding: utf-8 -*-
import sys
import random
import time
from memory_profiler import profile

if len(sys.argv) < 2:
    print("Usage: python 1-list_roop.py N")
    sys.exit(1)

N = int(sys.argv[1])
A = [[random.random() for j in range(N)] for i in range(N)]
B = [[random.random() for j in range(N)] for i in range(N)]
C = [[0 for j in range(N)] for i in range(N)]

@profile
def matrix_product():
    start = time.time()
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]
    end = time.time()
    print(f"Time: {end - start} sec")

matrix_product()
