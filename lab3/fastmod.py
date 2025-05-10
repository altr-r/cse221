def fast_mod_drift(a, b):
    result = 1
    mod = 107
    a = a % mod

    while b > 0:
        if b % 2 != 0:
            result = (result * a) % mod

        a = (a ** 2) % mod
        b = b // 2

    return result


a , b = list(map(int, input().split()))

print(fast_mod_drift(a, b))