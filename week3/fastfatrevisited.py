
def fast_mod_drift(base, exp, mod):
    if exp == 0:
        return 1
    binary = bin(exp)[2::]

    prev = base
    for i in range(1, len(binary)):
        if binary[i] == "1":
            quo = (prev ** 2) % mod
            prev = (quo * base) % mod
        elif binary[i] == "0":
            prev = (prev ** 2) % mod

    return prev


def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    T = int(data[0])
    index = 1

    for _ in range(T):
        a = int(data[index])
        n = int(data[index + 1])
        m = int(data[index + 2])
        index += 3

        sum_res = 0
        curr = a % m

        for i in range(1, n + 1):
            sum_res = (sum_res + curr) % m
            curr = fast_mod_drift(a, i + 1, m)

        print(sum_res)


solve()