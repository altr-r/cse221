n, m = list(map(int, input().split()))

first = list(map(int, input().split()))
second = list(map(int, input().split()))

out_degree = [0]*n
in_degree = [0]*n

for i in first:
    in_degree[i-1] += 1

for j in second:
    out_degree[j-1] += 1

for k in range(n):
    print(out_degree[k] - in_degree[k], end=" ")