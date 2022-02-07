from abc import ABC, abstractmethod
import queue
from typing import List
from typing_extensions import Self


class Graph(ABC):
    @abstractmethod()
    def __init__(self) -> Self:
        pass

    @abstractmethod()
    def adjacent(self, edge) -> list:
        pass


# we use an adjacency list
class Graph_adjacency:
    def __init__(self) -> Self:
        self.vertices: List[List] = []
        self.edges = []
        return self

    def __init__(self, vertices, edges) -> Self:
        self.vertices = vertices
        self.edges = edges
        return self

    def adjacent(self, edge):
        return self.vertices[edge]


def dfsFromVertex(G: Graph_adjacency, v, stack: list, visited):
    stack.append(v)
    while stack:
        u = stack.pop()
        if not visited[u]:
            visited[u] = True
            for w in G.adjacent():
                stack.append(w)


def dfs(G: Graph):
    visited = [
        False for _ in range(len(G.edges))
    ]  # this assumes that the label for each edge is a numerical id starting with id = 0
    stack = []
    for v in G.vertices:
        if not visited[v]:
            dfsFromVertex(G, v, stack, visited)


if __name__ == "__main__":
    # G = Graph_adjacency([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2, 4], [1, 2], [3]], [0, 1, 2, 3, 4, 5])
    G = Graph_adjacency(
        [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2, 4], [1, 2], [3]], [0, 1, 2, 3, 4, 5]
    )
    dfs(G)
