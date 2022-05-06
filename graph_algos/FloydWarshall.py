from asyncore import loop
import math
from random import randrange
import pprint


class GraphAdjacencyMatrix:
    def __init__(self, vertices, edges) -> None:
        self.vertices = vertices
        self.edges = edges


def floyd_warshall(
    G: GraphAdjacencyMatrix,
) -> "tuple[list[list[int]], list[list[int]]]":
    # this assumes that the unreachable sections are initialised to math.inf
    d_curr = G.edges

    d_next = d_curr

    # Initialise each previous node to -1
    pi_curr = [
        [-1 for _ in range(0, len(G.vertices))] for _ in range(0, len(G.vertices))
    ]

    # Set up distance from each node to itself to 0.
    # Set up the previous node to itself to itself.
    for i in range(0, len(G.vertices)):
        d_curr[i][i] = 0
        pi_curr[i][i] = i

    # For each edge, initialise the previously found edge
    for i in range(len(G.vertices)):
        for j in range(len(G.vertices)):
            if G.edges[i][j] != math.inf and G.edges[i][j] != 0:
                pi_curr[i][j] = i

    # Copy pi_curr
    pi_next = pi_curr

    # as seen in lectures.
    for k in range(0, len(G.vertices)):
        for i in range(0, len(G.vertices)):
            for j in range(0, len(G.vertices)):
                d_next[i][j] = d_curr[i][j]
                pi_next[i][j] = pi_curr[i][j]
                if j != i and (d_curr[i][k] + d_curr[k][j]) < d_next[i][j]:
                    d_next[i][j] = d_curr[i][k] + d_curr[k][j]
                    pi_next[i][j] = pi_curr[k][j]

        d_curr = [row[:] for row in d_next]  # deep copy

    return (d_next, pi_next)


def floyd_warshall_traced(
    G: GraphAdjacencyMatrix,
) -> "tuple[list[list[int]], list[list[int]]]":
    pp = pprint.PrettyPrinter(indent=2)
    print("Start:")
    # this assumes that the unreachable sections are initialised to math.inf
    d_curr = G.edges

    d_next = d_curr

    # Initialise each previous node to -1
    pi_curr = [
        [-1 for _ in range(0, len(G.vertices))] for _ in range(0, len(G.vertices))
    ]

    # Set up distance from each node to itself to 0.
    # Set up the previous node to itself to itself.
    for i in range(0, len(G.vertices)):
        d_curr[i][i] = 0
        pi_curr[i][i] = i

    # For each edge, initialise the previously found edge
    for i in range(len(G.vertices)):
        for j in range(len(G.vertices)):
            if G.edges[i][j] != math.inf and G.edges[i][j] != 0:
                pi_curr[i][j] = i

    # Copy pi_curr
    pi_next = pi_curr

    print("d_curr")
    pp.pprint(d_curr)
    print("pi_curr")
    pp.pprint(pi_curr)
    print("d_next")
    pp.pprint(d_next)
    print("pi_next")
    pp.pprint(pi_next)

    # as seen in lectures.
    for k in range(0, len(G.vertices)):
        print("step k")
        for i in range(0, len(G.vertices)):
            print("step i")
            for j in range(0, len(G.vertices)):
                print("step j")
                d_next[i][j] = d_curr[i][j]
                pi_next[i][j] = pi_curr[i][j]
                if j != i and (d_curr[i][k] + d_curr[k][j]) < d_next[i][j]:
                    d_next[i][j] = d_curr[i][k] + d_curr[k][j]
                    pi_next[i][j] = pi_curr[k][j]
                print("d_next")
                pp.pprint(d_next)
                print("pi_next")
                pp.pprint(pi_next)

        d_curr = [row[:] for row in d_next]  # deep copy

    return (d_next, pi_next)


def reconstruct_path(pi: "list[list[int]]", start: int, end: int) -> "list[int]":
    """
    Given the pi matrix returns the **Indices** for the vertices in the graph.
    You may need to loop through the graph's indices to get the values for path.
    """

    if pi[start][end] == -1:
        return []

    path = [end]
    while start != end:
        end = pi[start][end]
        path.append(end)

    return path[::-1]


def reconstruct_path_traced(pi: "list[list[int]]", start: int, end: int) -> "list[int]":
    """
    Given the pi matrix returns the **Indices** for the vertices in the graph.
    You may need to loop through the graph's indices to get the values for path.
    """

    if pi[start][end] == -1:
        return []

    path = [end]
    print("Start: \npath", path)
    while start != end:
        end = pi[start][end]
        path.append(end)
        print(path)

    return path[::-1]


# Example.
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
    path = []

    (d, pi) = floyd_warshall_traced(graph)

    # reconstruct to print the correct vertices
    # we use 4 and 1 when referring to 5 and 2, as the vertices are 1 indexed
    for x in reconstruct_path_traced(pi, 4, 1):
        path.append(graph.vertices[x])
    print(path)  # expected [5,4,2]
