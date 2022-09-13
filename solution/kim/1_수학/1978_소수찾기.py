def isprime(num):
    if num==1:
        return False
    for i in range(2,int(num**0.5)+1): #2부터 num의 제곱근의 int형 (더 작은 수까지)
        if num%i==0: #나눠지면 소수아님
            return False
    return True #for 다 돌고 나오면 true임.

len=int(input()) 
lst=map(int,input().split()) #공백 구분 리스트받음, type 전환해줘야함
sum=0
for i in lst:
    if isprime(i): #lst인덱스 i번째가 소수인지?
        sum+=1
print(sum)


