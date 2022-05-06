from queue import Queue
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


def bfs(G: GraphAdjacencyMatrix):
    visited = [None] * len(G.vertices)
    Q = Queue()
    for v in range(len(G.vertices)):
        if visited[v] is None:
            bfsFromVertex(G, v, visited, Q)


def bfsFromVertex(G, v, visited, Q):
    visited[v] = True
    Q.put(v)
    while not Q.empty():
        u = Q.get()  # dequeue
        for w in G.adjacents(u):
            if visited[w] is None:
                visited[w] = True
                Q.put(w)


def bfs_traced(G: GraphAdjacencyMatrix):
    print("Start:")
    print(str(G))
    visited = [None] * len(G.vertices)
    Q = Queue()
    print("Q", list(Q.queue))
    print("visited", visited)
    for v in range(len(G.vertices)):
        if visited[v] is None:
            bfsFromVertex_traced(G, v, visited, Q)


def bfsFromVertex_traced(G, v, visited, Q):
    print("bfsFromVertex")
    visited[v] = True
    Q.put(v)
    print("1 visited", visited)
    print("1 Q", list(Q.queue))
    while not Q.empty():
        u = Q.get()  # dequeue
        print("2 u", u)
        print("2 Q", list(Q.queue))
        for w in G.adjacents(u):
            if visited[w] is None:
                visited[w] = True
                Q.put(w)
                print("3 w, visited", w, visited)
                print("3 Q", list(Q.queue))


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

    bfs_traced(graph)
