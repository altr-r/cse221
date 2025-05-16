import heapq

n,m = map(int, input().split())

graph = {}

for i in range(1, n+1) :
    graph[i] = []

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra(G, vertex):
    s = 1
    distance = [float('inf') for _ in range(vertex + 1)]

    distance[s] = 0
    Q = []
    heapq.heappush(Q, (distance[s], s))
    while Q:
        currdist, u = heapq.heappop(Q)
        for v, d in G[u]:
            dist = max(currdist, d)
            if dist < distance[v]:
                distance[v] = dist
                heapq.heappush(Q, (distance[v], v))
    return distance

res = dijkstra(graph, n)[1:]

for i in res:
    if i == float('inf'):
        print(-1, end=" ")
    else:
        print(i, end=" ")