def minsort(arr):
    for i in range(len(arr)):
        flag = False
        for j in range(len(arr) - i - 1):
            if arr[j].split()[0] > arr[j+1].split()[0]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True

        if flag == False:
            break

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