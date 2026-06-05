nums = list(map(int, input().split()))

max_val = 0
min_val = 1001

for num in nums:
    if (num < 500 and num > max_val):
        max_val = num
    if (num > 500 and num < min_val):
        min_val = num

print(max_val, min_val)