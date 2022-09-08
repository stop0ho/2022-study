# 최대공약수
# 여러 수의 최대공약수 구하는 방법 생각해내지 못 해서 실패!
def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)
    
n, s = map(int, input().split())
a = list(map(int, input().split()))
for i in range(0, len(a)):
    if a[i] - s != 0:
        a[i] = abs(a[i] - s)

answer = 0
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        print(a[i], a[j])
        if gcd(a[i], a[j]) > answer:
            answer = gcd(a[i], a[j])
        print(answer)
            
print(answer)