# 메모리초과로 실패
from itertools import combinations_with_replacement

def prime_list(n): # n보다 작거나 같은 소수
    sieve = [True] * (n+1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False
    
    # 소수 목록 산출
    return [i for i in range(2, n+1) if sieve[i] == True]

t = int(input())
for i in range(t):
    n = int(input())
    ans = 0
    primes = prime_list(n)
    gold = list(combinations_with_replacement(primes, 2))
    for j in gold:
        if sum(j) == n:
            ans += 1
    print(ans)
    