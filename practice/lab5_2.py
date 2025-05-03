n, m = map(int, input().split())

first = list(map(int, input().split()))
second = list(map(int, input().split()))
third = list(map(int, input().split()))

list = {}

for i in range(1, n+1):
    list[i] = []

for i in range(len(first)):
    list[first[i]].append((second[i], third[i]))


for i in list.keys():
    if len(list[i]) == 0:
        print(f"{i}: ")
    else:
        print(f"{i}: ", end="")
        for j in list[i]:
            print(j, end=" ")
        print()