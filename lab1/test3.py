import sys

length = int(input())
arr = []

for _ in range(length):
    arr.append(sys.stdin.readline().replace("\n", ""))


for i in range(length):
    swap = False
    for j in range(length - i - 1):
        if arr[j].split()[0] > arr[j+1].split()[0]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swap = True
        elif (arr[j].split()[0] == arr[j + 1].split()[0]) and (arr[j].split()[6] < arr[j + 1].split()[6]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swap = True

    if swap == False:
        break



for dep in arr:
    print(dep)