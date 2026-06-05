n, m = map(int, input().split())

# Please write your code here.
maps = [[0 for _ in range(m)] for _ in range(n)]

num = 1

for start_col in range(m):
    cur_row = 0
    cur_col = start_col
    while (0 <= cur_col and cur_row < n):
        maps[cur_row][cur_col] = num

        cur_row += 1
        cur_col -= 1
        num += 1

for start_row in range(1, n):
    cur_row = start_row
    cur_col = m - 1
    while (0 <= cur_col and cur_row < n):
        maps[cur_row][cur_col] = num

        cur_row += 1
        cur_col -= 1
        num += 1

for i in range(n):
    print(*maps[i])