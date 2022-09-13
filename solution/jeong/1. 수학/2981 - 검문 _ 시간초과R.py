n = int(input())
nums = []

# m을 입력 받아서 nums에 넣음
for i in range(n):
    m = int(input())
    nums.append(m)
    

for div in range(2, max(nums)):
    new_list = []
    for num in nums:
        new_list.append(num % div)
    if len(set(new_list)) == 1:
        print(div, end = ' ')
