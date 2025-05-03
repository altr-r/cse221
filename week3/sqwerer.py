def find_max_wave(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return arr[left]


print(find_max_wave( [1,3, 4, 5, 9, 28, 2, -1]))