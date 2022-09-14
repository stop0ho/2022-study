#정수 개수, 부분수열의 합의 결과
#정수 개수 만큼 정수 리스트
n,sum=map(int,input().split())
lst=list(map(int,input().split()))
cnt=0

from itertools import combinations
comb=[]
for i in range(1,n+1): #부분수열 개수가 1~n개임.
    for j in combinations(lst,i): #조합값을 주더라도 i는 리스트가 아님. 
        print(j)
        if sum(j)==sum:
            cnt+=1
#중요한 점. i=1일 때, 원소개수 1개인 부분수열 -7, -3, -2, 5, 3 하나씩
#i=2면, (-7,-3), (-7,-2)..로 들어감.
#(-7,-3)도 결국엔 iterable임. sum() method로 합 구할 수 있음.

#print(cnt)
