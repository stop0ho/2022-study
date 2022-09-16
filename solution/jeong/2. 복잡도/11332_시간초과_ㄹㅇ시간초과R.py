def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def solution(oper, n, t, l):
    n, t, l = int(n), int(t), int(l)
    second = pow(10, 8) * l
    if oper == "O(N)":
        bigO = n*t
    elif oper == "O(2^N)":
        bigO = pow(2, n) * t
    elif oper == "O(N!)":
        bigO = fact(n) * t
    elif oper == "O(N^3)":
        bigO = pow(n, 3) * t
    elif oper == "O(N^2)":
        bigO = pow(n, 2) * t
    
    if second < bigO: print("TLE!")
    else: print("May Pass.")
        
c = int(input())
for _ in range(c):
    oper, n, t, l = input().split()
    solution(oper, n, t, l)
        