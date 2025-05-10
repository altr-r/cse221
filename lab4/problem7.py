import math

n, q = map(int, input().split())

matrix = []
for i in range(n):
    matrix.append([0]*n)

for i in range(1, n+1):
    for j in range(1, n+1):
        if i!=j and math.gcd(i, j) == 1:
            matrix[i-1][j-1] += j

neighbors = []

for i in range(len(matrix)):
    child = []
    for j in matrix[i]:
        if j != 0:
            child.append(j)
    neighbors.append(child)

for k in range(q):
    a, b = map(int, input().split())
    if b < n:
        print(neighbors[a-1][b-1])
    else:
        print("-1")