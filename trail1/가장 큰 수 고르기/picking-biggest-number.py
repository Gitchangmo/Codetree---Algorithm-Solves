import sys

nums = list(map(int, input().split()))

max_num = -sys.maxsize

for num in nums:
    if num > max_num:
        max_num = num

print(max_num)