cnt = 0
res = []

def hanoi(n, A, C, B):
    global cnt
    
    if n == 1:          #종료조건 : 하나만 있을 때 - 걍 A에서 C로 옮겨주면 됨
        res.append("{0} {1}".format(A, C))
        cnt += 1
        return
    
    hanoi(n-1, A, B, C)
    res.append("{0} {1}".format(A, C))
    cnt += 1
    hanoi(n-1, B, C, A)

n = int(input())
hanoi(n, 1, 3, 2)
print(cnt)
for i in res:
    print(i)