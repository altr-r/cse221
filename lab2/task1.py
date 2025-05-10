length, target = list(map(int, input().split()))

arr = list(map(int, input().split()))

def solve(arr):
    dict = {}

    for i in range(length):
        curr = arr[i]
        needed = target - curr

        if needed in dict:
            return (f"{dict[needed] + 1} {i + 1}")
        else:
            dict[curr] = i

    return -1


print(solve(arr))