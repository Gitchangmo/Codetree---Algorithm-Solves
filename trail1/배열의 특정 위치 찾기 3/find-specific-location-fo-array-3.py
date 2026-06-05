nums = list(map(int, input().split()))
temp = []

for i, num in enumerate(nums):
    if num == 0:
        break
    temp.append(num)

print(sum(temp[-1:-4:-1]))