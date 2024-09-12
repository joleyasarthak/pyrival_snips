def count_primes(n: int):
    # returns a dict containing all the prime factors of a number
    if n == 1:
        return []
    prime_counts = {}
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    if count > 0:
        prime_counts[2] = count
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            prime_counts[i] = count
    if n > 2:
        prime_counts[n] = 1
    return prime_counts
