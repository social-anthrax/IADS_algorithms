# Source: https://stackabuse.com/dijkstras-algorithm-in-python/

from queue import PriorityQueue


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [
            [-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)
        ]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight

    def dijkstra(self, start_vertex):
        D = {v: float("inf") for v in range(self.v)}
        pi = {v: None for v in range(self.v)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.v):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pi[neighbor] = current_vertex
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D

    def dijkstra_traced(self, start_vertex):
        print("Start:")

        # InitializeSingleSource
        D = {v: float("inf") for v in range(self.v)}
        pi = {v: None for v in range(self.v)}
        D[start_vertex] = 0
        #

        print("D", D)
        print("pi", pi)

        pq = PriorityQueue()
        pq.put((0, start_vertex))
        print("priority queue", pq)

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)

            # for x in Out(u) -> x == v  == neighbor
            for neighbor in range(self.v):
                # u == current_vertex
                if self.edges[current_vertex][neighbor] != -1:
                    #
                    # Relax
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        if old_cost == float("inf"):
                            print("inf at", neighbor)
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            # Q.insertItem(d[v], v) or Q.reduceKey(d[v], v)
                            pi[neighbor] = current_vertex
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
                    #
                print("step")
                print("D", D)
                print("pi", pi)
                print("priority queue", pq.queue)
        return D


if __name__ == "__main__":
    g = Graph(9)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 6, 7)
    g.add_edge(1, 6, 11)
    g.add_edge(1, 7, 20)
    g.add_edge(1, 2, 9)
    g.add_edge(2, 3, 6)
    g.add_edge(2, 4, 2)
    g.add_edge(3, 4, 10)
    g.add_edge(3, 5, 5)
    g.add_edge(4, 5, 15)
    g.add_edge(4, 7, 1)
    g.add_edge(4, 8, 5)
    g.add_edge(5, 8, 12)
    g.add_edge(6, 7, 1)
    g.add_edge(7, 8, 3)

    D = g.dijkstra_traced(0)
    print(D)
    # {0: 0, 1: 4, 2: 11, 3: 17, 4: 9, 5: 22, 6: 7, 7: 8, 8: 11}
