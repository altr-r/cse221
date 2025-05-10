def minsort(arr):
    for i in range(len(arr)):
        var = i
        for j in range(i + 1, len(arr)):
            if arr[j].split()[0] < arr[var].split()[0]:
                var = j

        if var != i:
            arr[i], arr[var] = arr[var], arr[i]

    for x in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j].split()[0] == arr[j + 1].split()[0] and arr[j].split()[6] < arr[j + 1].split()[6]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


N = int(input())
ram = []
for i in range(N):
    x = input()
    ram.append(x)

minsort(ram)

for i in ram:
    print(i)