nodes, edges = list(map(int, input().split()))

adjl = {}

for i in range(edges):
    node1, node2 = list(map(int, input().split()))
    if node1 not in adjl:
        adjl[node1] = [node2]
    else:
        adjl[node1] += [node2]

    if node2 not in adjl:
        adjl[node2] = [node1]
    else:
        adjl[node2] += [node1]


for keys in adjl:
    adjl[keys].sort()


def bfs(nodes, adjl):
    result = []
    queue = []

    visited = [False] * nodes

    queue.append(1)
    visited[0] = True

    while len(queue) != 0:
        currentElement = queue.pop(0)
        result.append(currentElement)

        for adjNodes in adjl[currentElement]:
            if not visited[adjNodes-1]:
                visited[adjNodes - 1] = True
                queue.append(adjNodes)

    for i in result:
        print(i, end=" ")

bfs(nodes, adjl)