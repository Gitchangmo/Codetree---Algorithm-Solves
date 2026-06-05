N, M = map(int, input().split())
arr = [[0 for _ in range(M)] for _ in range(N)]

count = 1

for i in range(N):
    for j in range(M):
        arr[i][j] = count

        count += 1

for i in arr:
    for j in i:
        print(j, end=' ')
    print()