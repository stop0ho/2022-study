def isprime(n): #소수인지 확인하는 함수
    if n == 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True


for _ in range(int(input())): #넣은 값만큼 돌아감
    num=int(input())
    a,b=num//2,num//2 #//는 몫임
    while a > 0:
        if isprime(a) and isprime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1