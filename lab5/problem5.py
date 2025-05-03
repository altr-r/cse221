import sys

sys.setrecursionlimit(2*100000+5)

nodes, edges = list(map(int, input().split()))

adjl = {}

for i in range(edges):
    node1, node2 = list(map(int, input().split()))
    if (node1 -1) not in adjl:
        adjl[node1 - 1] = [node2 - 1]
    else:
        adjl[node1 - 1].append(node2 - 1)


def solution(src, graph):
    visited[src] = 1

    for edge in graph.get(src, []):
        if visited[edge] == 0:
            if solution(edge, graph):
                return True
        elif visited[edge] == 1:
            return True

    visited[src] = 2

    return False

visited = [0] * nodes
cycle = False

for i in range(nodes):
    if visited[i] == 0:
        if solution(i, adjl):
            cycle = True
            break


if cycle is True:
    print("Yes")
else:
    print("No")