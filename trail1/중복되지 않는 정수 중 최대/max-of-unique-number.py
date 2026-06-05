n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
counter = [0] * 1001
temp = []

for num in nums:
    counter[num] += 1

for num in nums:
    if counter[num] == 1:
        temp.append(num)

if temp:
    print(max(temp))
else:
    print(-1)