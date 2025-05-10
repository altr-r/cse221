def solve(arr):
    i = 0
    j = length - 1

    while i < j:
        if arr[i] + arr[j] < target:
            i += 1
        elif arr[i] + arr[j] > target:
            j -= 1
        elif arr[i] + arr[j] == target:
            return f"{i + 1} {j + 1}"

    return -1


length, target = list(map(int, input().split()))

arr = list(map(int, input().split()))

print(solve(arr))