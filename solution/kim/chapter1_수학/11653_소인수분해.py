n=int(input())
#n보다 같거나 작은 소수리스트를 생성한다.
def isprime(num):
    if num==1:
        return False
    elif num==2 or num==3: #2는 소수이므로 이 부분을 추가한다.
        return True
    else:
        for i in range(2,int(num**0.5)+1): #3넣으면 range(2,2)여서 안됨
            if num%i==0: #예시 13은 2,3,4...로 안나눠짐
                return False
        return True # 이거는 for 나오고 생겨야함

prime=[]
for i in range(1,n+1):
    if isprime(i):
        prime.append(i)

#n이 2가될때까지 소인수분해한다. 1이면 break
while(n!=1):
    for i in prime: #n보다 작은 소수리스트의 앞꺼부터 소인수 분해함.
        if n%i==0: #인수라면?
            print(i)
            n=n/i
            break #continue를 하면 i=2에서 i=3으로 넘어감