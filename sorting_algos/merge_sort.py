from typing import List


def merge_sort(arr: List):  # O(n*log(n)), Master Theorem
    n = len(arr)
    if n < 2:
        return arr
    left = merge_sort(arr[: n // 2])  # O(n//2*log(n//2))
    right = merge_sort(arr[n // 2 :])  # O(n//2*log(n//2))
    return merge(left, right)  # O(n)


# We're merging backwards and then reversing the list because
# popping from/appending to the front is very inefficient.
def merge(left: List, right: List) -> List:  # O(n)
    merged = [None] * (len(left) + len(right))  # n = len(left) + len(right)
    i = 0
    j = 0
    for k in range(len(left) + len(right)):
        if len(left) > i and len(right) > j:
            if left[i] < right[j]:
                merged[k] = left[i]
                i = i + 1
            else:
                merged[k] = right[j]
                j = j + 1
        elif len(left) > i:
            merged[k] = left[i]
            i = i + 1
        elif len(right) > j:
            merged[k] = right[j]
            j = j + 1
        else:
            print("Uh oh, this shouldn't happen: i + j > len(left) + len(right)")
    return merged
    # while len(left) > 0 and len(right) > 0: # O(n) iterations
    #     if left[-1] > right[-1]:
    #         merged.append(left.pop())
    #     else:
    #         merged.append(right.pop())
    #         merged.extend(left) # O(len(left)) = O(n)
    #         merged.extend(right) # O(len(right)) = O(n)
    # return reversed(merged) # O(n)


def merge_sort_traced(arr: List):  # O(n*log(n)), Master Theorem
    print("Start:", arr)
    n = len(arr)
    if n < 2:
        print("final:", arr)
        return arr
    print("left from:", arr[: n // 2])
    left = merge_sort_traced(arr[: n // 2])  # O(n//2*log(n//2))
    print("right from:", arr[n // 2 :])
    right = merge_sort_traced(arr[n // 2 :])  # O(n//2*log(n//2))
    return merge_traced(left, right)  # O(n)


# We're merging backwards and then reversing the list because
# popping from/appending to the front is very inefficient.
def merge_traced(left: List, right: List) -> List:  # O(n)
    print("merge (L/R)")
    print(left)
    print(right)
    merged = [None] * (len(left) + len(right))  # n = len(left) + len(right)
    i = 0
    j = 0
    # A1 or B1 each mean 1 new comparison in the lecture implementation (not counting comparisons against infinity)
    for k in range(len(left) + len(right)):
        if len(left) > i and len(right) > j:
            if left[i] < right[j]:
                merged[k] = left[i]
                i = i + 1
                print("A1", merged)
            else:
                merged[k] = right[j]
                j = j + 1
                print("B1", merged)
        elif len(left) > i:
            merged[k] = left[i]
            i = i + 1
            print("A2", merged)
        elif len(right) > j:
            merged[k] = right[j]
            j = j + 1
            print("B2", merged)
        else:
            print("Uh oh, this shouldn't happen: i + j > len(left) + len(right)")
    print("merge done", merged)
    return merged
    # while len(left) > 0 and len(right) > 0: # O(n) iterations
    #     if left[-1] > right[-1]:
    #         merged.append(left.pop())
    #     else:
    #         merged.append(right.pop())
    #         merged.extend(left) # O(len(left)) = O(n)
    #         merged.extend(right) # O(len(right)) = O(n)
    # return reversed(merged) # O(n)


# def merge_traced(left: List, right: List) -> List: # O(n)
#     print("merge (L/R)")
#     print(left)
#     print(right)
#     merged = [] # n = len(left) + len(right)
#     while len(left) > 0 and len(right) > 0: # O(n) iterations
#         if left[-1] > right[-1]:
#             merged.append(left.pop())
#             print("A", merged)
#         else:
#             merged.append(right.pop())
#             print("B1", merged)
#             merged.extend(left) # O(len(left)) = O(n)
#             merged.extend(right) # O(len(right)) = O(n)
#             print("B2", merged)
#     print("merge done", list(reversed(merged)))
#     return list(reversed(merged)) # O(n)

if __name__ == "__main__":
    merge_sort_traced([1, 2, 3, 4, 5])
    merge_sort_traced([4, 3, 3, 2, 4, 5, 1])
