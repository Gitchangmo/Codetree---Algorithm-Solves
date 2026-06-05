nums = []
arr = list(map(int, input().split()))

for num in arr:
    if num >= 250:
        break
    nums.append(num)

Avg = sum(nums) / len(nums)
result = round(Avg, 1)

print(sum(nums), result)