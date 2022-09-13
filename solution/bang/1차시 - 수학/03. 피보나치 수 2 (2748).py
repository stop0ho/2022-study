# 입력값 n을 받는다.
n = int(input())

# 초기값 a, b 값을 지정함.
a = 0
b = 1

# 반복문을 통해 피보나치 수의 합을 구한다.
for i in range(1, n):
    val = a + b
    a, b = b, val

if n == 0:
    print(a)
elif(n == 1):
    print(b)
else:
    print(val)