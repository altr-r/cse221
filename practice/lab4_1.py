n, m = map(int, input().split())

matrix = []

for i in range(n):
    matrix.append([0]*n)


for i in range(m):
    fro, to, cost = list(map(int, input().split()))
    matrix[fro - 1][to - 1] = cost


for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()