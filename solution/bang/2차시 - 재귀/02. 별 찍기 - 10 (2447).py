# 별찍기 재귀 함수
def recursion(n):
    if n == 1:
        return ['*']
    
    val = recursion(n//3)
    L = []
    
    for i in val:
        L.append(i*3)
    for i in val:
        L.append(i+' '*(n//3)+i)
    for i in val:
        L.append(i*3)
    
    return L

N = int(input())
print('\n'.join(recursion(N)))