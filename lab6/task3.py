from collections import deque


def path(N, x1, y1, x2, y2):
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    if x1 == x2 and y1 == y2:
        return 0

    directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    visited = [[-1] * N for _ in range(N)]
    queue = deque()
    queue.append((x1, y1))
    visited[x1][y1] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1 :
                visited[nx][ny] = visited[x][y] + 1
                if nx == x2 and ny == y2:
                    return visited[nx][ny]
                queue.append((nx, ny))

    return -1


n = int(input())

xf, yf, xt, yt = map(int, input().split())
print(path(n, xf, yf, xt, yt))