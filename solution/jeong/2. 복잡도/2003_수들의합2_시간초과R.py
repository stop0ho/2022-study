# 투포인터 써야한다고 함.

n, m = map(int, input().split())
nums = list(map(int, input().split()))

res = 0

for i in range(0, len(nums)):
    for j in range(i, len(nums)):
        if sum(nums[i:j+1]) == m:
            res += 1
            
print(res)