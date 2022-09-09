# 두 수를 입력받는다.
a, b = map(int, input().split())

# 이후 최소 공배수를 구하기 위해 두 값을 곱해둔다.
LCM = a*b

# 유클리드 호제법을 사용하기 위해 항상 a>b가 되도록 만든다.
if a < b:
    a,b = b,a

# 유클리드 호제법을 활용하여 최대 공약수를 구한다.
c = a%b
while(True):
    if c == 0:
        break
    else:
        c = a%b
        a, b = b, c
GCD = a
print(GCD)

# 최대 공약수를 알면 최소 공배수는 쉽게 구할 수 있다.
# LCM = 값1 * 값2 / GCD
print(int(LCM/GCD))