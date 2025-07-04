def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped :
            break
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1 :
        return arr
    mid  = len(arr) // 2
    left_helf = merge_sort(arr[:mid])
    right_helf = merge_sort(arr[mid:])
    return merge(left_helf, right_helf)

def merge(left, right):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot :
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def Quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        Quick_sort(arr, low, pi - 1)
        Quick_sort(arr, pi + 1, high)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest] :
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i :
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def build_heap(arr, n):
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

def heap_sort(arr):
    n = len(arr)
    build_heap(arr, n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

arr1 = [60, 40, 50, 30, 10, 20]
print("Selection sort", end = " : ")
print(selection_sort(arr1))              # 10 20 30 40 50 60

arr2 = [60, 40, 50, 30, 10, 20]
print("Bubble sort", end = " : ")
print(bubble_sort(arr2))                 # 10 20 30 40 50 60

arr3 = [60, 40, 50, 30, 10, 20]
print("Insertion sort", end = " : ")
print(insertion_sort(arr3))              # 10 20 30 40 50 60

arr4 = [60, 40, 50, 30, 10, 20]
print("Merge sort", end = " : ")
print(merge_sort(arr4))                  # 10 20 30 40 50 60

arr5 = [60, 40, 50, 30, 10, 20]
print("Quick sort", end=" : ")
Quick_sort(arr5, 0, len(arr5) - 1)
print(arr5)                              # 10 20 30 40 50 60

arr6 = [60, 40, 50, 30, 10, 20]
heap_sort(arr6)
print(arr6)                              # 10 20 30 40 50 60