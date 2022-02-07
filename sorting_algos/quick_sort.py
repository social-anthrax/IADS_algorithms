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


print(driver([9, 4, 2, 5, 1, 8, 4]))
print(driver([4, 3, 2, 1, 8, 3, 9, 4, 3, 2, 1, 9, 4, 103, 34, 1234, 4]))
