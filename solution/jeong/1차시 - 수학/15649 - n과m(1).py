from itertools import permutations
a, b = map(int, input().split())
nums = list(range(1, a+1))

for i in permutations(nums, b):
    for j in range(0, b):
        print(i[j], end=' ')
    print()