# 입력값 N을 받아들인다.
N = int(input())

for i in range(1,N+1):
    l = ' '*(N-i)+'*'*i
    print(l)
    
for i in range(N-1,0,-1):
    l = ' '*(N-i)+'*'*i
    print(l)