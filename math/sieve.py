def sieve(n):
    s = [1] * (n + 1)
    x = []
    for i in range(2, n + 1):
        if s[i]:
            x.append(i)
            for j in range(i, n + 1, i):
                s[j] = 0
    return x