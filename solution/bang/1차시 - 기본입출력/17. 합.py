# 입력 값 n을 받아들인다.
n = int(input())
val = 0

# 반복문을 이용해서 1부터 n까지 더한다.
for i in range(1, n+1):
    val += i
    
print(val)
