import heapq

n, m, s, d = map(int, input().split())

graph = {}

for i in range(1, n + 1):
    graph[i] = []

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))


def second_shortest_path(n, s, d, graph):
    dist1 = [float('inf')] * (n + 1)
    dist2 = [float('inf')] * (n + 1)

    dist1[s] = 0
    pq = [(0, s)]

    while pq:
        cost, u = heapq.heappop(pq)

        for v, w in graph[u]:

            if cost + w < dist1[v]:
                dist2[v] = dist1[v]
                dist1[v] = cost + w
                heapq.heappush(pq, (dist1[v], v))
            elif dist1[v] < cost + w < dist2[v]:
                dist2[v] = cost + w
                heapq.heappush(pq, (dist2[v], v))

    if dist2[d] == float('inf'):
        return -1
    else:
        return dist2[d]


print(second_shortest_path(n, s, d, graph))
