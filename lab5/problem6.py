row,col = map(int,input().split())

matrix = []
for i in range(row):
    inp = input()
    temp = []
    for i in inp:
        temp.append(i)
    matrix.append(temp)


def bfs(x, y, grid, visited, r, c):
    queue = []
    queue.append((x, y))
    visited[x][y] = True
    if grid[x][y] == "D":
        diamond_count = 1
    else:
        diamond_count = 0

    while queue:
        x, y = queue.pop(0)

        if (0 <= x - 1 < r) and (0 <= y < c):
            if visited[x - 1][y] == False and grid[x - 1][y] != '#':
                visited[x - 1][y] = True
                queue.append((x - 1, y))
                if grid[x - 1][y] == 'D':
                    diamond_count += 1

        if (0 <= x + 1 < r) and (0 <= y < c):
            if  visited[x + 1][y] == False and grid[x + 1][y] != '#':
                visited[x + 1][y] = True
                queue.append((x + 1, y))
                if grid[x + 1][y] == 'D':
                    diamond_count += 1

        if (0 <= x < r) and (0 <= y - 1 < c):
            if visited[x][y - 1] == False and grid[x][y - 1] != '#':
                visited[x][y - 1] = True
                queue.append((x, y - 1))
                if grid[x][y - 1] == 'D':
                    diamond_count += 1

        if (0 <= x < r) and (0 <= y + 1 < c):
            if visited[x][y + 1] == False and grid[x][y + 1] != '#':
                visited[x][y + 1] = True
                queue.append((x, y + 1))
                if grid[x][y + 1] == 'D':
                    diamond_count += 1

    return diamond_count


visited = []
for i in range(row):
    visited.append([False] * col)

max_diamonds = 0
for i in range(row):
    for j in range(col):
        if not visited[i][j] and matrix[i][j] != '#':
            diamonds = bfs(i, j, matrix, visited, row, col)
            max_diamonds = max(max_diamonds, diamonds)


print(max_diamonds)

