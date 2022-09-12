#베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다
def isprime(num):
    if num==1:
        return False
    for i in range(2,int(num**0.5)+1): #2부터 num의 제곱근의 int형 (더 작은 수까지)
        if num%i==0: #나눠지면 소수아님
            return False
    return True #for 다 돌고 나오면 true임.

while True:
    num=int(input())
    cnt=0
    for i in range(num+1,2*num+1): #n+1과 2n사이에서, 그 값이 소수면 카운트함.
        if isprime(i): cnt+=1
    print(cnt) 
    # for 구문이 나올때마다 isprime함수가 돌아야하므로 비효율적임