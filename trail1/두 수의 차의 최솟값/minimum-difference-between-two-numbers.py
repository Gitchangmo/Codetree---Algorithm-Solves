N = int(input())
nums = list(map(int, input().split()))

min_val = 101

for i in range(len(nums)-1):
    for j in range(i, len(nums)):
        if nums[i] == nums[j]:
            continue
        if nums[j] - nums[i] < min_val:
            min_val = nums[j] - nums[i]

print(min_val)
