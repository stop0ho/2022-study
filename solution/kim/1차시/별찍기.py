n = int(input())
for i in range(1, n+1):
    if(i==1 or i==n):   #1과 n일때가 특수한 상황이므로 if문 처리
        print(" " * (n-i) + "*" * (2*i-1))
    else:
        print(" " * (n-i) + "*" + " " * (2*(i-1)-1) + "*")