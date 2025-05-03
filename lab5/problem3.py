nodes, edges, source, destination = list(map(int, input().split()))

adjl = {}

first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))

for i in range(len(first_list)):
    if first_list[i] in adjl:
        adjl[first_list[i]] += [second_list[i]]
    else:
        adjl[first_list[i]] = [second_list[i]]

for j in range(len(second_list)):
    if second_list[j] in adjl:
        adjl[second_list[j]] += [first_list[j]]
    else:
        adjl[second_list[j]] = [first_list[j]]

for i in range(1, nodes + 1):
    if i not in adjl:
        adjl[i] = []

for keys in adjl:
    adjl[keys].sort()


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
        print(-1)
        return

    current = dest

    while current != 0:
        path.append(current)
        current = parent[current]

    print(distance[dest])

    path.reverse()
    for i in path:
        print(i, end=" ")


solution(nodes, source, destination, adjl)