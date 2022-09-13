def prime_list(n): # n보다 작거나 같은 소수
    sieve = [True] * (n+1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False
    
    # 소수 목록 산출
    return [i for i in range(2, n+1) if sieve[i] == True]

'''
# 시간초과
k = int(input())
for i in range(k):
    n = int(input())
    primes = prime_list(n)
    sub = primes[len(primes)-1] - primes[0]
    
    for m in primes:
        for l in primes:
            if m + l == n and abs(m - l) < sub:
                sub = abs(m-l)
                part_a = m
                part_b = l
    
    print(part_a, part_b)
'''