from itertools import combinations

n, m = map(int, input().split())
nums = list(range(1, n+1))
for i in combinations(nums, m):
    for j in range(0, m):
        print(i[j], end=' ')
    print()