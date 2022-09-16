import math

# 입력값 받기
N, M = map(int, input().split())
A = list(map(int, input().split()))

# 이동할 수 있는 최대 거리 D를 구하기 위한 사전 작업
l = A[:]
l.append(M)
l.sort()

# D 구하는 알고리즘, 최대공약수를 구하는 funtion 활용
arr = []
for i in range(0, N):
    arr.append(l[i+1]-l[i])

print(math.gcd(*arr))