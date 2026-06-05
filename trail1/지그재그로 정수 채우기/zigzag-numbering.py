n, m = map(int, input().split())

# Please write your code here.
maps = [[0 for _ in range(m)] for _ in range(n)]

num = 0
flag = 1
for i in range(m):
    if flag % 2 == 1:
        for j in range(n):
            maps[j][i] = num
            num += 1
    else:
        for j in range(n-1,-1,-1):
            maps[j][i] = num
            num += 1
    flag += 1

for i in range(n):
    print(*maps[i])