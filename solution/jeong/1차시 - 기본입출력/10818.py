n = int(input())
nums = input()
nums = nums.split()

for i in range(n):
  nums[i] = int(nums[i])

print(min(nums), max(nums))

# 추가로 생각해볼 것 : split하면서 넣을 때 그냥 형변환 하는 방법은 없나?