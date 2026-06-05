N = int(input())

arr = [[1 for _ in range(N)] for _ in range(N)]

for row in range(1, N):
    for col in range(1, N):
        arr[row][col] = arr[row-1][col-1] + arr[row-1][col] + arr[row][col-1]

for i in range(N):
    print(*arr[i])