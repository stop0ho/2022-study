#자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

from itertools import permutations
num,m=map(int,input().split())
n=list(range(1,num+1))
for i in permutations(n,m): #n이 리스트이므로 i값도 리스트임
    for j in i:
        print(j, end=' ') #기존 조합은 (1,2,)로 출력되는걸 1 2로 바꿈
    print() #한줄 돌고 줄띄움


