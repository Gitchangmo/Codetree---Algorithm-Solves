nums = list(map(int, input().split()))

arr = [0] * 7

for num in nums:
    arr[num] += 1

for i in range(1, 7):
    print(f"{i} - {arr[i]}")