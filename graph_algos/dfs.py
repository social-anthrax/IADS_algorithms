from queue import LifoQueue
import math


class GraphAdjacencyMatrix:
    def __init__(self, vertices, edges) -> None:
        self.vertices = vertices
        self.edges = edges

    def __str__(self):
        return (
            "Vertices: "
            + str(self.vertices)
            + "\n"
            + "\n".join([str(edge) for edge in self.edges])
        )

    def adjacents(self, i):
        return [i for i, w in enumerate(self.edges[i]) if w != math.inf]


def dfs(G: GraphAdjacencyMatrix):
    visited = [None] * len(G.vertices)
    # Stack!
    S = LifoQueue()
    for v in range(len(G.vertices)):
        if visited[v] is None:
            dfsFromVertex(G, v, visited, S)


def dfsFromVertex(G, v, visited, S):
    visited[v] = True
    S.put(v)
    while not S.empty():
        u = S.get()  # dequeue
        for w in G.adjacents(u):
            if visited[w] is None:
                visited[w] = True
                S.put(w)


def dfs_traced(G: GraphAdjacencyMatrix):
    print("Start:")
    print(str(G))
    visited = [None] * len(G.vertices)
    # Stack!
    S = LifoQueue()
    print("Q", list(S.queue))
    print("visited", visited)
    for v in range(len(G.vertices)):
        if visited[v] is None:
            dfsFromVertex_traced(G, v, visited, S)


def dfsFromVertex_traced(G, v, visited, S):
    print("dfsFromVertex")
    visited[v] = True
    S.put(v)
    print("1 visited", visited)
    print("1 Q", list(S.queue))
    while not S.empty():
        u = S.get()  # dequeue
        print("2 u", u)
        print("2 Q", list(S.queue))
        print("2 adjacents", G.adjacents(u))
        for w in G.adjacents(u):
            if visited[w] is None:
                visited[w] = True
                S.put(w)
                print("3 w, visited", w, visited)
                print("3 Q", list(S.queue))


if __name__ == "__main__":
    weights = [
        [0, math.inf, 6, 3, math.inf],
        [3, 0, math.inf, math.inf, math.inf],
        [math.inf, math.inf, 0, 2, math.inf],
        [math.inf, 1, 1, 0, math.inf],
        [math.inf, 4, math.inf, 2, 0],
    ]

    vertices = [1, 2, 3, 4, 5]
    graph = GraphAdjacencyMatrix(vertices, weights)
    dfs_traced(graph)

    weights2 = [
        [0, math.inf, math.inf, math.inf, 1],
        [1, 0, math.inf, 1, 1],
        [1, math.inf, 0, 1, 1],
        [math.inf, math.inf, math.inf, 0, 1],
        [math.inf, math.inf, math.inf, math.inf, math.inf],
    ]

    vertices2 = [1, 2, 3, 4, 5]
    graph2 = GraphAdjacencyMatrix(vertices2, weights2)

    dfsFromVertex_traced(graph2, 0, [None] * len(vertices2), LifoQueue())
