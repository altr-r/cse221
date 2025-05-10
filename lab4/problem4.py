n, m = list(map(int, input().split()))

first = list(map(int, input().split()))
second = list(map(int, input().split()))


mat = [0]*n

for i in range(m):
    mat[first[i] - 1] +=1
    mat[second[i] - 1] += 1


odd_degree = 0
even_degree = 0

for count in mat:
    if count % 2 != 0:
        odd_degree += 1
    else:
        even_degree += 1


if even_degree == n or odd_degree == 2:
    print("YES")
else:
    print("NO")