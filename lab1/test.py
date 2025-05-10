length = int(input())

ids = list(map(int, input().split()))
marks = list(map(int, input().split()))


cnt = 0
arr = []


for i in range(length):
    arr.append((ids[i], marks[i]))

for j in range(length):
    max = j
    k = j + 1
    while k < length:
        if arr[k][1] > arr[max][1] or (arr[k][1] == arr[max][1] and arr[k][0] < arr[max][0]):
            max = k
        k += 1

    if max != j:
        arr[j], arr[max] = arr[max], arr[j]
        cnt += 1

print(f"Minimum swaps: {cnt}")

for i in arr:
    print(f"ID: {i[0]} Mark: {i[1]}")