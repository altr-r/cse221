import sys
sys.setrecursionlimit(2*100000+5)


nodes, edges = list(map(int, input().split()))
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

def dfs(source, graph, isVisited, result):
    isVisited[source - 1] = True
    result.append(source)

    for edges in graph[source]:
        if visited[edges - 1] == False:
            dfs(edges, graph, isVisited, result)


visited = [False] * nodes
result = []

dfs(1, adjl, visited, result)
for i in result:
    print(i, end=" ")