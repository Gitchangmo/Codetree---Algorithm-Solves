N = int(input())

arr = [0] * 10

nums = list(map(int, input().split()))

for num in nums:
    arr[num] += 1

for i in range(1, 10):
    print(arr[i])