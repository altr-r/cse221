
def solution():

    n, m = map(int,input().split())

    edges = []
    for _ in range(m):
        u,v,w = map(int, input().split())
        edges.append((w, u, v))

    edges.sort()

    parent = [i for i in range(n + 1)]
    rank = [0] * (n + 1)

    total_cost = 0
    for w, u, v in edges:
        if union(u, v, parent, rank):
            total_cost += w

    print(total_cost)


def find(u, parent):
    if parent[u] != u:
        parent[u] = find(parent[u], parent)
    return parent[u]

def union(u, v, parent, rank):
    ru = find(u, parent)
    rv = find(v, parent)
    if ru == rv:
        return False
    if rank[ru] < rank[rv]:
        parent[ru] = rv
    else:
        parent[rv] = ru
        if rank[ru] == rank[rv]:
            rank[ru] += 1
    return True

solution()
