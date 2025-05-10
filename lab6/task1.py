from collections import deque

def solution(n, m, graph, inDegree):
    queue = deque()

    for i in range(1, n + 1):
        if inDegree[i] == 0:
            queue.append(i)

    result = []

    while queue:
        curr = queue.popleft()
        result.append(curr)

        for neigh in graph[curr]:
            inDegree[neigh] -= 1

            if inDegree[neigh] == 0:
                queue.append(neigh)

    if len(result) == n:
        for i in result:
            print(i, end=" ")
    else:
        print(-1)


n, m = map(int, input().split())

graph = {}
inDegree = [0] * (n + 1)

for i in range(1, n+1):
    graph[i] = []

for i in range(m):
    fro, to = map(int, input().split())

    graph[fro].append(to)
    inDegree[to] += 1


solution(n, m, graph, inDegree)