n, m = list(map(int, input().split()))

mat = []

for i in range(n):
    mat.append([0]*n)

for i in range(m):
    node1, node2, cost = list(map(int, input().split()))
    mat[node1-1][node2-1] = cost

for i in range(n):
    for j in range(n):
        print(mat[i][j], end=" ")
    print()