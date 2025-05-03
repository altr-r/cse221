n = int(input())
matrix = []
for i in range(n):
    matrix.append([0]*n)

given = []

for i in range(n):
    given.append(list(map(int, input().split()))[1:])

for i in range(n):
    for j in given[i]:
        matrix[i][j] = 1

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()


