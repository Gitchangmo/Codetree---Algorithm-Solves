N = int(input())

nums = list(map(int, input().split()))

temp = [num ** 2 for num in nums]

print(*temp, end='')