import sys
from itertools import combinations

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    
    len = arr[0]
    
    for a in combinations(arr[1:len++1], 6):
        temp = list(map(int, a))
        for i in temp:
            print(i, end = ' ')
        print()
    print()
    
# print(' '.join(temp))