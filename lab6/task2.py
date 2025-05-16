n, m = map(int, input().split())

graph = {}

for i in range(1, n + 1):
    graph[i] = []

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

vis = [False] * (n + 1)
col = [-1] * (n + 1)

mxGrp = 0

def solve(source):
    q = []

    q.append(source)
    col[source] = 0
    cnt = [1, 0]
    vis[source] = True

    while q:
        curr = q.pop(0)
        for adj in graph[curr]:
            if vis[adj] == False:
                col[adj] = 1 - col[curr]
                cnt[col[adj]] += 1
                vis[adj] = True
                q.append(adj)
            elif col[adj] == col[curr]:
                return 0
    return max(cnt)

for i in range(1, n + 1):
    if vis[i] == False:
        mxGrp += solve(i)

print(mxGrp)