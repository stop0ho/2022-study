def gcd(a, b):
    r = a % b
    if r == 0:      #종료조건
        return b
    else:
        return gcd(b, r)

def lcm(a, b): #최소공배수 = 두 자연수의 곱/최대공약수
    return int(a*b/gcd(a,b))

a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))