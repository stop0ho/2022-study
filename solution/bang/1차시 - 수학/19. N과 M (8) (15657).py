from itertools import combinations_with_replacement

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

a = []
for i in combinations_with_replacement(arr, M):
    a.append(i)

a = list(set(a))

a.sort()

for i in a:
    for j in i:
        print(j, end=" ")
    print()