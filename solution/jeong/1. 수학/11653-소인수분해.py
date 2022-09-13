def prime_list(n): # n보다 작거나 같은 소수
    sieve = [True] * (n+1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False
    
    # 소수 목록 산출
    return [i for i in range(2, n+1) if sieve[i] == True]

n = int(input())
primes = prime_list(n)
nums = []

while n > 1:
    for i in primes:
        if n%i == 0:
            nums.append(i)
            n /= i
            continue
        
nums.sort()
for i in nums:
    print(i)
