nums = [list(map(int, input().split())) for _ in range(2)]

arr1 = []
arr2 = []
arr3 = []

for i in range(2):
    Avg = sum(nums[i]) / 4
    arr1.append(f"{Avg:.1f}")

for i in range(4):
    Avg = (nums[0][i] + nums[1][i]) / 2
    arr2.append(f"{Avg:.1f}")

temp = 0
for i in range(2):
    temp += sum(nums[i])

Avg = temp / 8

print(*arr1)
print(*arr2)
print(f"{Avg:.1f}")
