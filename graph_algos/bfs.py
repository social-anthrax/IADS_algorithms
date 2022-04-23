# Graph as Adjacency List
n = 8
G = [[1,4],
    [0,2,5],
    [1,3,5,6,7],
    [2,6],
    [0,5,6],
    [1,2,4],
    [2,3,4,7],
    [2,6]]
visited = [0] * n
q = []
def bfs(G):
    for v in range (0,n):
        if visited[v] == 0:
            visited[v] = 1
            print("---\nVisit",v)
            q.append(v)
            print("queue",q)
            while len(q)>0:
                u = q.pop(0) # pop front of queue
                print("queue",q)
                for w in G[u]:
                    if visited[w] == 0:
                        visited[w] = 1
                        print("Visit",w)
                        q.append(w)
                        print("queue",q)
            

bfs(G)
