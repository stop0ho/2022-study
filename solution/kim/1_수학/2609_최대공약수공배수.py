a,b=map(int,input().split())
#최대공약수
deva=[]
devb=[]
for i in range(1,int(a/2)+1): #1부터 그 수의 반까지만 확인
    if a%i==0: deva.append(i)
deva.append(a) #본인 값도 약수이므로

for i in range(1,int(b/2)+1): #b도 같은 방식
    if b%i==0: devb.append(i)
devb.append(b)

for i in reversed(devb): #b의 약수 리스트를 역으로 뽑아 
    if deva.count(i)==1: #a 약수 리스트에 있으면, 최대공약수
        print(i)
        break #1은 약수리스트에 서로 있으므로 고려 x

#최소공배수
mula=[]
mulb=[]
for i in range(1,b+1): #a*b가 최대값인 최소공배수이므로
    mula.append(a*i)
for i in range(1,a+1): #마찬가지
    mulb.append(b*i)

for i in mulb: #먼저나오는거니까 역순 필요 없음
    if mula.count(i)==1:
        print(i)
        break
