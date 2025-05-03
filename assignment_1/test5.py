str = "ABCD will departure for Chittagong at 01:00"
str_2 = "ABCD will departure for Mymensingh at 00:30"

print(str.split()[6] > str_2.split()[6] )


# .split(":")[0]


# for k in range(length - 1):
#     if (arr[k].split()[0] == arr[k + 1].split()[0]) and (arr[k].split()[6].split(":")[0] < arr[k+1].split()[6].split(":")[0]):
#         arr[k], arr[k+1] = arr[k+1], arr[k]