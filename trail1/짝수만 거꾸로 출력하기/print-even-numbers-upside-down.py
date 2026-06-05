N = int(input())
nums = list(map(int, input().split()))
temp = []

for num in nums:
    if num % 2 == 0:
        temp.append(num)

print(*temp[::-1])