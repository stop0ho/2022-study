from itertools import permutations

arr = ['A', 'B', 'C', 'D']


for i in permutations(arr, 2):
    print(i)
    
    
print(list(permutations(arr, 2)))
