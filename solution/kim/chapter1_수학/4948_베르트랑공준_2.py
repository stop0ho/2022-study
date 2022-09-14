lst=[]

#소수 판별함수
def isprime(num):
    if num==1:
        return False
    if num==2:
        return True
    for i in range(2,int(num**0.5)+1): #2부터 num의 제곱근의 int형 (더 작은 수까지)
        if num%i==0: #나눠지면 소수아님
            return False
    return True #for 다 돌고 나오면 true임.

#입력값 리스트 만들기
while True:
    n=int(input())
    if n==0:
        break
    else:
        lst.append(n)

prime=[]
#입력값 중 가장 큰 수보다 작은 소수 리스트 만들기
for i in range(2,max(lst)+1): #2부터 lst 최대값까지
    if isprime(i):
        prime.append(i)

#소수 리스트에서 n+1보다 작은 소수를 제거하고 그 길이를 반환한다.

    for i in prime:
        if i<n+1:
            prime.remove(i)
        else:
            break

    print(len(prime))

# 이 방법 쓰면, 길이가 작아져 점점 값이 이상해지므로 쓸 수 없음.