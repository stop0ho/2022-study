# 입력값 N을 받아들인다.
N = int(input())

for i in range(1,N+1):
    l = ' '*(N-i)+'*'*((2*i)-1)
    print(l)