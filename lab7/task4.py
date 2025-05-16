import heapq


n, m, s, d = map(int,input().split())

weights = list(map(int, input().split()))

graph = {}

for i in range(1, n + 1):
    graph[i] = []

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

def beautiful_path(n, s, d, graph, weights):
    dist = [float('inf')] * (n + 1)
    dist[s] = weights[s-1]

    pq = [(dist[s], s)]

    while pq:
        distance, u = heapq.heappop(pq)

        if distance > dist[u]:
            continue

        for v in graph[u]:
            if distance + weights[v-1] < dist[v]:
                dist[v] = distance + weights[v-1]
                heapq.heappush(pq, (dist[v], v))

    if dist[d] == float('inf'):
        print(-1)
    else:
        print(dist[d])

beautiful_path(n, s, d, graph, weights)