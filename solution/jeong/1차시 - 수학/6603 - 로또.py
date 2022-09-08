# 조합
from itertools import combinations
while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    for i in list(combinations(nums[1:], 6)):
        for j in i:
            print(j, end=' ')
        print()
    print()