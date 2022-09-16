#recursion를 활용한 factorial 구현

# factorial 함수
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
        
# 입력
N = int(input())

#출력 
print(factorial(N))
