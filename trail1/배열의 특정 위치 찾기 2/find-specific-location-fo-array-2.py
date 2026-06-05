nums = list(map(int, input().split()))
N = len(nums)

A = []
B = []

for i in range(0, N, 2):
    A.append(nums[i])

for i in range(1, N, 2):
    B.append(nums[i])

if sum(A) > sum(B):
    print(sum(A) - sum(B))
else:
    print(sum(B) - sum(A))