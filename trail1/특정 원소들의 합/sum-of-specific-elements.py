maps = [list(map(int, input().split())) for _ in range(4)]

total_sum = 0

for i in range(4):
    for j in range(i+1):
        total_sum += maps[i][j]

print(total_sum)
