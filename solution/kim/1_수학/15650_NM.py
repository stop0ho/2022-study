#수열만들기 
from itertools import combinations as cb
n,r=map(int,input().split())
lst=list(range(1,n+1)) # 1~n 까지의 리스트

for i in cb(lst,r): #리스트 중 r개 뽑기
    for j in i: #combination 출력 시 튜플을 기본으로 바꿔주는 법
        print(j,end=' ')
    print()