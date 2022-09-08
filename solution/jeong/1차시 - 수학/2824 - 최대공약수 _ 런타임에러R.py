# 런타임 에러

def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)
    
n = int(input())
a_list = list(map(int, input().split()))
m = int(input())
b_list = list(map(int, input().split()))

a = 1
b = 1

for i in a_list:
    a *= i

for i in b_list:
    b *= i

print(str(gcd(a,b))[-9:])