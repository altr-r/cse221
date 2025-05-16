import heapq

n, m, s, d = map(int,input().split())

graph = {}

for i in range(1, n + 1):
    graph[i] = []

first = list(map(int, input().split()))
second = list(map(int, input().split()))
weights = list(map(int, input().split()))

for i in range(len(first)):
    graph[first[i]].append((second[i], weights[i]))

def shortest_path(n, s, d, graph):
    dist = [float('inf')] * (n + 1)
    dist[s] = 0

    pq = [(0, s)]

    parent = [-1] * (n + 1)

    while pq:
        distance, u = heapq.heappop(pq)

        if distance > dist[u]:
            continue

        for v, weight in graph[u]:
            if distance + weight < dist[v]:
                dist[v] = distance + weight
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    if dist[d] == float('inf'):
        print(-1)
    else:
        print(dist[d])
        curr = d
        path = []
        while curr != -1:
            path.append(curr)
            curr = parent[curr]
        for i in range(-1, -len(path) - 1, -1):
            print(path[i], end=" ")

shortest_path(n, s, d, graph)