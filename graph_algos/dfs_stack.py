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

def dfs_stack(G):
    for v in range(0,n):
        if visited[v] == 0:
            s.append(v)
            print("stack",s)
            while len(s)>0:
                u = s.pop() # get most recently added
                print("stack",s,"<- popped")
                if visited[u]==0:
                    visited[u] = 1
                    print("---\nVisit",u)
                    for w in G[u]:
                        s.append(w)
                        print("stack",s)

dfs_stack(G)