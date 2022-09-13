from itertools import combinations

n, s = map(int, input().split())
nums = list(map(int, input().split()))
comb = []
ans = 0

for i in range(1, n+1):
    for j in combinations(nums, i):
        comb.append(j)

for i in comb:
    if sum(i) == s:
        ans += 1
        
print(ans)