# -*- coding: utf-8 -*-
from memory_profiler import profile
import numpy as np

output_dir = {
    "default": './npSize/defalut.txt',
}

@profile
def generate_list():
    arr = np.zeros((34, 366))
    result_list = []
    for i in range(55):
        result_list.append(arr)
        mem_usage = np.array(result_list).nbytes
        with open(output_dir["default"], 'a') as f:
            f.write(f"{mem_usage}\n")
    return result_list


@profile    
def main():
    newlist = generate_list()
    del newlist
    print("type defalut END")

if __name__ == '__main__':
    main()
