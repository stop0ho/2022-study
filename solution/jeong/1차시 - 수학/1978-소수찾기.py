def primeNumber(x):
    if x==1:
        return False
    for i in range(2, int(x**1/2) + 1):
        if x%i == 0:
            return False
    return True

n = int(input())
numbers = list(map(int, input().split()))
sum = 0

for i in numbers:
    if primeNumber(i):
        sum += 1
        
print(sum)
