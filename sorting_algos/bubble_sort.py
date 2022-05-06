from typing import List


def bubble_sort(arr: List):  # O(n**2)
    for n in range(len(arr), 1, -1):  # O(n) iterations
        for i in range(n - 1):  # O(n) iterations
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


def bubble_sort_traced(arr: List):  # O(n**2)
    print("Start:", arr)
    for n in range(len(arr), 1, -1):  # O(n) iterations
        for i in range(n - 1):  # O(n) iterations
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            print(arr)
    print("final", arr)


if __name__ == "__main__":
    bubble_sort_traced([1, 2, 3, 4, 5])
    bubble_sort_traced([4, 3, 3, 2, 4, 5, 1])
