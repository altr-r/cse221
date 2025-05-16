import sys

sys.setrecursionlimit(2 * 10 ** 5 + 5)

nodes, root = map(int, input().split())
graph = {}

for i in range(1, nodes + 1):
    graph[i] = []

for i in range(nodes - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

size = [0] * (nodes + 1)


def dfs(node, parent):
    size[node] = 1
    for adjl in graph[node]:
        if adjl != parent:
            dfs(adjl, node)
            size[node] += size[adjl]


dfs(root, -1)

query = int(input())
for i in range(query):
    inp = int(input())
    print(size[inp])