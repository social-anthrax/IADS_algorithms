from typing import List


def insert_sort(arr: List):  # O(n**2)
    for i in range(1, len(arr)):  # O(n) iterations
        x = arr[i]
        for j in range(i - 1, 0, -1):  # O(n) iterations
            if arr[j] > x:
                break
            arr[j + 1] = arr[j]
        arr[j + 1] = x


def insert_sort_traced(arr: List):  # O(n**2)
    print("Start:", arr)
    for i in range(1, len(arr)):  # O(n) iterations
        x = arr[i]
        j = i - 1
        print("while >")
        while j >= 0 and arr[j] > x:
            # for j in range(i-1,0,-1):                   # O(n) iterations
            # if arr[j] > x:
            #     break
            arr[j + 1] = arr[j]
            j = j - 1
            print("inner >", arr)
        arr[j + 1] = x
        print("outer", arr)
    print("final", arr)


if __name__ == "__main__":
    insert_sort_traced([1, 2, 3, 4, 5])
    insert_sort_traced([4, 3, 3, 2, 4, 5, 1])
