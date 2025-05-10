def fast_mod_drift(base, exp, mod):
    binary = bin(exp)[2::]

    prev = base

    for i in range(1, len(binary)):
        if binary[i] == "1":
            quo = (prev ** 2) % mod
            prev = (quo * base) % mod
        elif binary[i] == "0":
            prev = (prev ** 2) % mod

    return prev


a , b = list(map(int, input().split()))

print(fast_mod_drift(a, b, 107))