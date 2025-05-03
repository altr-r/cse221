def bubblesort(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for i in range(n - 1):
            if arr[i].split()[0] > arr[i + 1].split()[0]:  # Sorting by first word
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
            elif arr[i].split()[0] == arr[i + 1].split()[0]:  # Tie-breaking based on 7th word
                if arr[i].split()[6] < arr[i + 1].split()[6]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True


N = int(input())
ram = [input() for _ in range(N)]
print(ram)
bubblesort(ram)

for i in ram:
    print(i)
