MOD = 10**9+7
def binpow(a: int, b: int) -> int:
    res = 1
    while b > 0:
        if b & 1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        b >>= 1
    return res