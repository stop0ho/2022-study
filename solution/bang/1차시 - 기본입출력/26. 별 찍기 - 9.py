# 입력값 N을 받아들인다.
N = int(input())

for i in range(0,N):
    l = ' '*i+'*'*(2*(N-i)-1)
    print(l)
    
for i in range(N-2,-1,-1):
    l = ' '*i+'*'*(2*(N-i)-1)
    print(l)