
def solve():
    N, K = map(int, input().split())

    parent = [i for i in range(N + 1)]
    size = [1] * (N + 1)

    result = []
    for _ in range(K):
        a, b = map(int, input().split())
        result.append(str(union(a, b, parent, size)))

    for i in result:
        print(i)


def find(u, parent):
    if parent[u] != u:
        parent[u] = find(parent[u], parent)
    return parent[u]


def union(u, v,parent, size):
    ru = find(u, parent)
    rv = find(v, parent)
    if ru == rv:
        return size[ru]
    if size[ru] < size[rv]:
        ru, rv = rv, ru
    parent[rv] = ru
    size[ru] += size[rv]
    return size[ru]


solve()
