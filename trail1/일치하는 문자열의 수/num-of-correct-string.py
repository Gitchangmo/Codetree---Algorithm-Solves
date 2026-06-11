n, A = input().split()
n = int(n)

count = 0

for _ in range(n):
    S = input()
    if S == A:
        count += 1

print(count)