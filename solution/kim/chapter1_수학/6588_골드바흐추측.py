#4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
#소수 판별 함수
def isprime(num):
    if num==1:
        return False
    elif num==2 or num==3: #2는 소수이므로 이 부분을 추가한다.
        return True
    else:
        for i in range(2,int(num**0.5)+1): #3넣으면 range(2,2)여서 안됨
            if num%i==0: #예시 13은 2,3,4...로 안나눠짐
                return False
        return True

#이번엔 b-a가 가장 큰 것. (차이 젤 심하게)
while True:
    n=int(input()) #입력 조건은 6<=n<=100000으로 정해짐.
    if n==0: break
    else:
        a,b=1,n-1 #가장 작은 홀수, 가장 큰 홀수
        while True: #둘 다 소수일 때 멈춤
            if isprime(a) and isprime(b):
                break
            else:
                a+=2
                b-=2
        print(n,'=',a,'+',b)

#isprime은 시간이 오래걸리는 함수임. 소수리스트 만들어서 그 안에 있는 값인지 확인.
