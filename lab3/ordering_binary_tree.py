def ordering_binary_tree(arr, left, right):
    res = []
    if left > right:
        return []

    mid = (left + right) // 2

    res.append(arr[mid])

    arr1 = ordering_binary_tree(arr, left, mid - 1)
    arr2 = ordering_binary_tree(arr, mid+1, right)

    return res + arr1 + arr2



length = int(input())
arr = list(map(int, input().split()))
left = 0
right = length - 1


result = ordering_binary_tree(arr, left, right)
for i in result:
    print(i, end=" ")