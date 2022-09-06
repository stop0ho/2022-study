# 입력값 N을 받아들인다.
N = int(input())

for i in range(1, N+1):
    print(' '* (N-i), end = '')
    for j in range(i): 
        print('*', end = ' ')
    print()