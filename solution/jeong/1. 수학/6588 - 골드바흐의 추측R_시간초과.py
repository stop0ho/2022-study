# 중복조합
from itertools import combinations_with_replacement

def prime_list(n): # n보다 작거나 같으며 홀수인 소수
    sieve = [True] * (n+1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False
    
    # 소수 목록 산출
    return [i for i in range(3, n+1) if sieve[i] == True]

while True:
    n = int(input())
    if n == 0:
        break
    primes = prime_list(n)
    gold = list(combinations_with_replacement(primes, 2))
    max = 0
    ans_a = 0
    ans_b = 0
    for i in gold:
        a = i[0]
        b = i[1]
        if a + b == n and b-a > max:
            ans_a = a
            ans_b = b
            max = b-a
    if ans_a == 0 and ans_b == 0:
        print("Goldbach's conjecture is wrong.")
    else:
        print("{0} = {1} + {2}".format(n, ans_a, ans_b))