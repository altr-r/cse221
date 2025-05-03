vertices, edges, source, destination, through = list(map(int, input().split()))

adj_list = {}

for i in range(edges):
    vertex1, vertex2 = map(int, input().split())

    if vertex1 in adj_list:
        adj_list[vertex1] += [vertex2]
    else:
        adj_list[vertex1] = [vertex2]

for i in range(1, vertices + 1):
    if i not in adj_list:
        adj_list[i] = []

for i in adj_list:
    adj_list[i].sort()


def solution(nodes, src, dest, graph):
    queue = []
    head = 0
    visited = [False] * (nodes + 1)

    parent = [0] * (nodes + 1)
    distance = [float('-inf')] * (nodes+1)

    path = []

    queue.append(src)
    visited[src] = True
    distance[src] = 0

    while head < len(queue):
        elem = queue[head]
        head+=1

        for edg in graph[elem]:
            if visited[edg] == False:
                visited[edg] = True
                parent[edg] = elem
                distance[edg] = distance[elem] + 1
                queue.append(edg)


    if not visited[dest]:
        return -1, path

    current = dest

    while current != 0:
        path.append(current)
        current = parent[current]


    path.reverse()

    return distance, path

dist_src_to_k, path_to_k = solution(vertices, source, through, adj_list)
dist_k_to_dest, path_to_dest = solution(vertices, through, destination, adj_list)

if dist_src_to_k == -1 or dist_k_to_dest == -1:
    print(-1)
else:
    result = path_to_k + path_to_dest[1:]
    print(len(result) - 1)
    for i in result:
        print(i, end=" ")