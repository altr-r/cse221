import heapq

n, m = map(int, input().split())

graph = {}
for i in range(1, n + 1):
    graph[i] = []

first = list(map(int, input().split()))
second = list(map(int, input().split()))
weights = list(map(int, input().split()))

for i in range(m):
    graph[first[i]].append((second[i], weights[i]))

def parity_edges(n, graph):
    s = 1
    d = n

    dist = []

    for _ in range(n + 1):
        dist.append([float('inf')] * 2)
    pq = []

    for v, w in graph[s]:
        parity = w % 2
        if w < dist[v][parity]:
            dist[v][parity] = w
            heapq.heappush(pq, (w, v, parity))

    while pq:
        cost, u, last_parity = heapq.heappop(pq)

        for v, w in graph[u]:
            new_parity = w % 2
            if new_parity == last_parity:
                continue
            if cost + w < dist[v][new_parity]:
                dist[v][new_parity] = cost + w
                heapq.heappush(pq, (dist[v][new_parity], v, new_parity))

    result = min(dist[d][0], dist[d][1])

    if result != float('inf'):
        print(result)
    else:
        print(-1)

parity_edges(n, graph)
