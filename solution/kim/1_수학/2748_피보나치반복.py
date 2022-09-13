n=int(input())
if n==0: print(0)
elif n==1: print(1)
else:
    n0=0
    n1=1
    for i in range(2,n+1):
        n2=n0+n1
        n0=n1
        n1=n2
    print(n2)

    '''
N = int(input())
A = [i for i in range(N+1)] #1부터 N까지 수를 바로 리스트 만듦
A[1] = 1

for i in range(2, N+1) :
    A[i] = A[i-1] + A[i-2] #0과 1의 값으로 나머지 리스트를 만듦
    
print(A[-1]) #리스트 마지막 값 출력
    '''