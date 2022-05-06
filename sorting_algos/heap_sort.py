from typing import List
from heapq import heappush, heappop, heapify

# using minheap
def heapsort(arr: List) -> List:
    h = []
    for value in arr:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]


def heapsort_traced(arr: List) -> List:
    print("Start:", arr)
    arr = [-x for x in arr]
    n = len(arr)

    heapify(arr)
    print("Heapified:", [-x for x in arr])

    final = []
    print(final)
    for i in range(n - 1, -1, -1):
        v = heappop(arr)
        final.append(v)
        print(list(reversed([-x for x in final])))

    print("heapsort done", list(reversed([-x for x in final])))
    return final


if __name__ == "__main__":
    heapsort_traced([1, 2, 3, 4, 5])
    heapsort_traced([4, 3, 3, 2, 4, 5, 1])

# def heap_sort(arr): # O(n*log(n))
#     n = len(arr)
#     heapify(arr, n) # O(n)
#     for i in range(n): # O(n) iterations
#         arr[-i] = extract_max(arr, n-1) # O(log(n))
