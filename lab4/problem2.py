n, m = list(map(int, input().split()))

first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))


result = [0]*n

for i in range(m):
    if result[first[i] - 1] == 0:
        result[first[i] - 1] = [(second[i], third[i])]
    else:
        result[first[i] - 1] += [(second[i], third[i])]



for i in range(len(result)):
    if result[i] == 0:
        print(f"{i+1}: ")
    else:
        print(f"{i+1}: ",end="")
        for j in result[i]:
            print(j, end=" ")
        print()