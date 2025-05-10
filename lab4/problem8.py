import math

n, q = map(int, input().split())

matrix = []
for i in range(n):
    matrix.append([0]*n)

for i in range(1, n+1):
    for j in range(1, n+1):
        if i != j and math.gcd(i, j) == 1:
            matrix[i-1][j-1] = 1


neighbors = []

for i in range(n):
    child = []
    for j in range(n):
        if matrix[i][j] == 1:
            child.append(j+1)
    neighbors.append(sorted(child))

for k in range(q):
    a, b = map(int, input().split())
    if b <= len(neighbors[a - 1]):
        print(neighbors[a - 1][b - 1])
    else:
        print("-1")
