import sys
nums = list(map(int, input().split()))

max_val = -sys.maxsize
min_val = sys.maxsize

for num in nums:
    if (num == 999 or num == -999):
        break
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print(max_val, min_val)