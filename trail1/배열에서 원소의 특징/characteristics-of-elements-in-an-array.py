nums = list(map(int, input().split()))

for idx, num in enumerate(nums):
    if num % 3 == 0:
        print(nums[idx-1])
        break