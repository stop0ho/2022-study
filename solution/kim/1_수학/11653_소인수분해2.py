n=int(input())
i=2 #2부터 시작해 1씩 증가시켜 소인수로 나타낼 것
while n!=1:
    if n%i==0:
        n=n/i
        print(i)
    else: i+=1