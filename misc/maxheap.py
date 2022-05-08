import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout
import os


def maxHeapify(arr, i):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l < len(arr) and arr[l] > arr[i]:
        largest = l
    if r < len(arr) and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, largest)


def heapExtractMax(arr):
    ret = arr[0]
    arr[0], arr[-1] = arr[-1], arr[0]
    maxHeapify(arr, 0)
    return ret


def heapMaximum(A):
    return A[0]


def parent(j):
    return (j - 1) // 2


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def maxHeapInsert(A, k):
    A.append(k)
    j = len(A) - 1
    while j != 0 and A[j] > A[(j - 1) // 2]:
        A[j], A[(j - 1) // 2] = A[(j - 1) // 2], A[j]


def buildMaxHeap(A):
    for i in range(len(A) // 2, -1, -1):
        maxHeapify(A, i)


def draw_tree(list):
    G = nx.DiGraph()
    G.add_nodes_from(list)
    for i in range(len(list) // 2):
        G.add_edge(list[i], list[(i << 1) + 1])
        G.add_edge(list[i], list[(i << 1) + 2])

    plt1, ax = plt.subplots(figsize=(10, 10))
    pos = graphviz_layout(G, prog="dot")
    nx.draw(G, pos, with_labels=True, ax=ax)
    plt1.show()
    input()
    # plt1.savefig(os.path.join(os.getcwd(), "maxheap.png")) # uncommment to save tree.


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5, 6, 7]  # put ur list here

    buildMaxHeap(list)
    print(list)
    draw_tree(
        list
    )  # put this anywhere during runtime to visualise tree during intermediary steps.
    
    # os.system("maxheap.png")
    # set up visualisation
