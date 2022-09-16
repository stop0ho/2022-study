# 실패
arr = []
num = []

N = int(input())
for _ in range(N):
    arr.append(int(input()))

for m in range(2, int(max(arr)**(1/2))+1):
    val = []
    for i in arr:
        val.append(i%m)
    if len(set(val)) == 1:
        print(m, end = ' ')