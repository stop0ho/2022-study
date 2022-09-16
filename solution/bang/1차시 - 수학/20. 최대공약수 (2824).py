N = int(input())
n = list(map(int, input().split()))

M = int(input())
m = list(map(int, input().split()))

def gcd(a,b) :
    while b > 0 :
        tmp = a%b
        a = b
        b = tmp
    return a

def multiply(arr):
    t = 1
    for i in arr:
        t *= i
    return t

a = multiply(n)
b = multiply(m)

print('%s'%str(gcd(a, b))[-9:])