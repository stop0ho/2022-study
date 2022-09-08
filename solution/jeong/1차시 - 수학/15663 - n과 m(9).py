from itertools import permutations

n, m = map(int, input().split())
nums = list(map(int, input().split()))

p = list(set(permutations(nums, m)))
p.sort()

for i in p:
    for j in i:
        print(j, end = ' ')
    print()