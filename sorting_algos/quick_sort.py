from typing import List


def QuickSort(array: List, left: int, right: int):
    if left < right:
        split = partition(array, left, right)
        QuickSort(array, left, split - 1)
        QuickSort(array, split + 1, right)


def partition(array: List, low: int, high: int):
    pivot = array[high]
    i = low - 1
    for j in range(low, high, 1):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]  # swap A[i+1] and A[high]
    return i + 1


def driver(A: List):
    QuickSort(A, 0, len(A) - 1)
    return A


def QuickSort_traced(array: List, left: int, right: int):
    print("qs", left, right, array)
    if left < right:
        split = partition_traced(array, left, right)
        QuickSort_traced(array, left, split - 1)
        QuickSort_traced(array, split + 1, right)


def partition_traced(array: List, low: int, high: int):
    pivot = array[high]
    print("pivot index, pivot", high, pivot)
    print("array", array)
    i = low - 1
    for j in range(low, high, 1):
        if array[j] <= pivot:
            i = i + 1
            print("swap", i)
            array[i], array[j] = array[j], array[i]
        print("after loop step", i, j, array)
    print("swap: final, after loop")
    array[i + 1], array[high] = array[high], array[i + 1]  # swap A[i+1] and A[high]
    print(array)
    return i + 1


def driver_traced(A: List):
    print("Start:", A)
    QuickSort_traced(A, 0, len(A) - 1)
    return A


print(driver([9, 4, 2, 5, 1, 8, 4]))
print(driver([4, 3, 2, 1, 8, 3, 9, 4, 3, 2, 1, 9, 4, 103, 34, 1234, 4]))

print(driver_traced([9, 4, 2, 5, 1, 8, 4]))
print(driver_traced([4, 3, 2, 1, 8, 3, 9, 4, 3, 2, 1, 9, 4, 103, 34, 1234, 4]))

print(partition_traced([1, 3, 11, 6, 15, 7], 0, 5))
