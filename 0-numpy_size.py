# -*- coding: utf-8 -*-
from memory_profiler import profile
import numpy as np
import tensorflow as tf

output_dir = {
    np.float16: './npSize/float16.txt',
    np.float32: './npSize/float32.txt',
    np.float64: './npSize/float64.txt',
    np.int8: './npSize/int8.txt',
    np.int16: './npSize/int16.txt',
    np.int32: './npSize/int32.txt',
    np.int64: './npSize/int64.txt',
    np.uint8: './npSize/uint8.txt',
    np.uint16: './npSize/uint16.txt',
    np.uint32: './npSize/uint32.txt',
    np.uint64: './npSize/uint64.txt',
    np.bool_: './npSize/np.bool_.txt',
    bool: './npSize/bool.txt',
}

@profile
def generate_list(dtype):
    arr = np.zeros((34, 366), dtype=dtype)
    result_list = []
    for i in range(55):
        arr = tf.stack(arr)
        arr = tf.reshape(arr, [1, 34, 366, 1]) 
        result_list.append(arr[0])
        

        # result_list.append(arr)
        mem_usage = np.array(result_list).nbytes
        with open(output_dir[dtype], 'a') as f:
            f.write(f"{mem_usage}\n")
    return result_list

@profile    
def main():
    for dtype in [np.float16, np.float32, np.float64, np.int8, np.int16, np.int32, np.int64, np.uint8, np.uint16, np.uint32, np.uint64, bool]:
        newlist = generate_list(dtype)
        del newlist
        print("type", dtype, "END")

if __name__ == '__main__':
    main()
