import heapq

n,m,s,t = map(int, input().split())

graph = {}

for i in range(1, n+1) :
    graph[i] = []

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))



def dijkstra(G, s, vertex):
    distance = [float('inf') for _ in range(vertex + 1)]

    distance[s] = 0
    Q = []
    heapq.heappush(Q, (distance[s], s))
    while Q:
        u = heapq.heappop(Q)[1]
        for v, d in G[u]:
            if distance[v] > distance[u] + d:
                distance[v] = distance[u] + d
                heapq.heappush(Q, (distance[v], v))
    return distance

distance_from_s = dijkstra(graph, s, n)
distance_from_t = dijkstra(graph, t, n)

minimumTime = float('inf')
node = -1

for v in range(1, n+1):
    if distance_from_s[v] != float('inf') and distance_from_t[v] != float('inf'):
        time = max(distance_from_s[v], distance_from_t[v])
        if time < minimumTime or (time == minimumTime and v < node):
            minimumTime = time
            node = v

if node == -1:
    print(-1)
else:
    print(f"{minimumTime} {node}")