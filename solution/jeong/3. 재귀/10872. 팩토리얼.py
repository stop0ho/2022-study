def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)


n = int(input())
print(fact(n))


a = int(input("숫자를 입력해주세요 : "))
