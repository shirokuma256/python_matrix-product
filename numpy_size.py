# python -m memory_profiler generate_list.py > result.csv

from memory_profiler import profile
import numpy as np

@profile
def generate_list(dtype):
    arr = np.zeros(50, dtype=dtype)
    arr_list = arr.tolist()
    del arr
    return arr_list

# generate_list(np.uint8)
# generate_list(bool)

for dtype in [bool, np.float16, np.float32, np.float64, np.int8, np.int16, np.int32, np.int64, np.uint8, np.uint16, np.uint32, np.uint64]:
    generate_list(dtype)
