N, M = map(int, input().split())

maps = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c = map(int, input().split())

    maps[r-1][c-1] = r*c

for i in range(N):
    print(*maps[i])