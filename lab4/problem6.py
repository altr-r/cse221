n = int(input())

x, y = map(int, input().split())

valid_moves = []

if (1 <= x - 1 <= n) and (1 <= y - 1 <= n):
    valid_moves.append((x-1, y-1))
if (1 <= x - 1 <= n) and (1 <= y <= n):
    valid_moves.append((x-1, y))
if (1 <= x - 1 <= n) and (1 <= y + 1 <= n):
    valid_moves.append((x-1, y+1))
if (1 <= x <= n) and (1 <= y - 1 <= n):
    valid_moves.append((x, y-1))
if (1 <= x <= n) and (1 <= y + 1 <= n):
    valid_moves.append((x, y+1))
if (1 <= x + 1 <= n) and (1 <= y - 1 <= n):
    valid_moves.append((x+1, y-1))
if (1 <= x + 1 <= n) and (1 <= y <= n):
    valid_moves.append((x+1, y))
if (1 <= x + 1 <= n) and (1 <= y + 1 <= n):
    valid_moves.append((x+1, y+1))

print(len(valid_moves))
for i in valid_moves:
    print(i[0], i[1])