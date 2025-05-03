len1 = int(input())
arr1 = list(map(int, input().split()))

len2 = int(input())
arr2= list(map(int, input().split()))

i = 0
j = 0
arr = []

while i < len1 and j < len2:
    if arr1[i] <= arr2[j]:
        arr.append(arr1[i])
        i+=1
    elif arr1[i] > arr2[j]:
        arr.append(arr2[j])
        j+=1

if i != len1:
    for indx in range(i, len1):
        arr.append(arr1[indx])
elif j != len2:
    for indx in range(j, len2):
        arr.append(arr2[indx])

for i in arr:
    print(i, end=" ")