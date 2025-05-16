from collections import deque

n = int(input())

graph = {}

for i in range(1, n+1):
    graph[i] = []


for i in range(n-1):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def solve(start, n, graph, visited):
    q = deque([start])
    visited[start] = 0
    far = start
    maxdiameter = 0

    while q:
        u = q.popleft()
        for v in graph[u]:
            if visited[v] == -1:
                visited[v] = visited[u] +1
                q.append(v)
                if visited[v]> maxdiameter:
                    maxdiameter = visited[v]
                    far = v
    return far, maxdiameter

visited = [-1]*(n+1)
x, y = solve(1, n, graph, visited)

visited = [-1] * (n + 1)
z, diame = solve(x, n, graph, visited)

print(diame)
print(x, z)