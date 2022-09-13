from itertools import permutations

for i in permutations(list(map(int, input().split())), 2):
    print(i)