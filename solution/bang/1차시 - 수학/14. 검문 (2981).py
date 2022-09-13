'''
A = M * a + R
B = M * b + R
C = M * c + R 일때

A - B = M ( a - b )
B - C = M ( b - c ) 이다.

M을 구하는 것이 문제의 해답이므로
A-B와 B-C의 최대 공약수를 구하고
1을 제외한 약수를 모두 출력하면 된다.
'''

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