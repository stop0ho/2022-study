# 입력값 N을 받아들인다.
N = int(input())

# 소인수분해 진행
while(True):
    if N == 1:
        break
    else:
        for i in range(2, N+1):
            if N%i == 0:
                print(i)
                N = int(N/i)
                break
            


"""
# 방법 2

N = int(input())
while(N != 1):
    for i in range(2, N+1):
        if N%i == 0:
            print(i)
            N = int(N/i)
            break
            
# 방법 3

N = int(input())
m = 2
while N != 1:
    if N%m == 0:
        print(m)
        N = int(N/m)
    else:
        m += 1
"""                