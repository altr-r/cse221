def merge(a, b):
    output = []
    inv = 0
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            output.append(b[j])
            inv += 1
            j += 1
        else:
            output.append(a[i])
            i += 1

    for n in range(i, len(a)):
        output.append(a[n])
    for m in range(j, len(b)):
        output.append(b[m])

    return output, inv


def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        mid = len(arr) // 2
        a1, inv1 = mergeSort(arr[0:mid])
        a2, inv2 = mergeSort(arr[mid:])
        merged, inv3 = merge(a1, a2)

        return merged, (inv1 + inv2 + inv3)

N = int(input())
arr = list(map(int, input().split()))
sorted, inv_count = mergeSort(arr)
print(inv_count)
for i in sorted:
    print(i, end=" ")