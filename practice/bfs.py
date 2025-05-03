v, e = map(int, input().split())

matrix = [[0] * v for _ in range(v)] # matrix = [] for i in range(vertices): matrix.append([0]*vertices)

def adjMat(edges):
    for i in range(e):
        f, t = map(int, input().split())

        matrix[f][t] = 1
        matrix[t][f] = 1


def adjList(v, e):
    list = [[] for _ in range(v)]
    for i in range(e):
        f, t = map(int, input().split())

        list[f].append(t)
        list[t].append(f)
    return list





def BFS(source, graph, vertices):
    q = []
    q.append(source)

    visited = [False]*vertices

    visited[source] = True

    res = []
    while len(q) != 0:
        u = q.pop(0)
        res.append(u)

        for i in graph[u]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)

    return res

lsit = adjList(v, e)
print("result" , BFS(0, lsit, v))