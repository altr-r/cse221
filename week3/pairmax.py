times = int(input())

arr = list(map(int, input().split()))

maximum = float('-inf')

i = 0
for j in range(1, len(arr)):
    maximum = max(maximum, arr[i] + arr[j] ** 2)

    i = arr.index(max(arr[i], arr[j]))


print(maximum)