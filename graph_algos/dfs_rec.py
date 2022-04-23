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
s = []

def dfsFromVertex(G,v):
    print("Visit",v)
    visited[v] = 1
    for w in G[v]:
        if visited[w] == 0:
            dfsFromVertex(G,w)
            print("Recurse back",v)
def dfs_rec (G):
    for v in range(0,n):
        if visited[v] == 0:
            print("---\nNew Start:",v)
            dfsFromVertex(G,v)

dfs_rec(G)
