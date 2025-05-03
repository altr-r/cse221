def binary_search_first(arr, key):
    left, right = 0, len(arr) - 1

    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] < key:
            left = mid + 1
        elif arr[mid] > key:
            right = mid - 1
        else:
            result = mid
            right = mid - 1

    count = 0

    for i in range(result, len(arr)):
        if arr[i] == key:
            count += 1
        else:
            break


    return (result, count)


arr = [1, 2, 2, 4, 5, 6, 7]
print(binary_search_first(arr, 2))