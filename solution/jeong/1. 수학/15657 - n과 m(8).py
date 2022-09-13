# 중복 조합
from itertools import combinations_with_replacement

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

for i in combinations_with_replacement(nums, m):
    for j in i:
        print(j, end = ' ')
    print()