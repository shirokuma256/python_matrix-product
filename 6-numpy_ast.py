# -*- coding: utf-8 -*-
import sys
import numpy as np
from memory_profiler import profile
import time

@profile
def matrix_multiplication():

    if len(sys.argv) < 2:
        print("Usage: python 1-list_roop.py N")
        sys.exit(1)

    N = int(sys.argv[1])

    # 行列のサイズ
    # N = 1000

    # 2つのランダムな行列を生成
    matrix1 = np.random.rand(N, N)
    matrix2 = np.random.rand(N, N)

    # 計算時間を計測
    start_time = time.time()

    # 行列積を計算
    result_matrix = matrix1 * matrix2

    # 計算時間を計測
    end_time = time.time()
    elapsed_time = end_time - start_time

    # 計算結果と計算時間を表示
    print(f"Result matrix:\n{result_matrix}\n")
    print(f"Elapsed time: {elapsed_time:.5f} seconds")

if __name__ == '__main__':
    matrix_multiplication()
