def DFS(source, graph):
    stack = []
    stack.append(source)

    visited = [False] * len(graph)
    res = []

    while len(stack) != 0:
        s = stack.pop()

        if visited[s] == False:
            res.append(s)
            visited[s] = True

        for node in graph[s]:
            if visited[node] == False:
                stack.append(node)

    return res


v, e = map(int, input().split())
def adjList(v, e):
    list = [[] for _ in range(v)]
    for i in range(e):
        f, t = map(int, input().split())

        list[f].append(t)
        list[t].append(f)
    return list

lsit = adjList(v, e)
print(DFS(0, lsit))
