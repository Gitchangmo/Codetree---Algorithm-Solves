N = int(input())

maps = [[0 for _ in range(N)] for _ in range(N)]
num = 1
flag = 1

for i in range(N-1, -1, -1):
    if flag % 2 == 1:
        for j in range(N-1, -1, -1):
            maps[j][i] = num
            num += 1
            flag = 0
    else:
        for j in range(N):
            maps[j][i] = num
            num += 1
            flag = 1

for i in range(N):
    print(*maps[i])