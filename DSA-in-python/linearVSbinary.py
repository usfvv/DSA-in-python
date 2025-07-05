import numpy as np
import time

def linear_search(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return f"Your item {arr[i]} is found"
    return f"your item {item} not found"

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return f"your element is found :{arr[mid]}"
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return f"your element is not found {target}"
        

arr_1 = np.arange(150000000)
linear_start = time.time()
result_l = linear_search(arr_1, 1000000000)
print(f"linear search time: {time.time() - linear_start} ")  #linear search time: 21.39298677444458 

binary_start = time.time()
result_b = binary_search(arr_1, 1000000000)
print(f"binary search time: {time.time() - binary_start} ")  #binary search time: 0.0 
