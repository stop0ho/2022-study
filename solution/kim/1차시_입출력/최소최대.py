len = int(input())
nums = input().split()

for i in range(len):
  nums[i] = int(nums[i])

print(min(nums), max(nums))