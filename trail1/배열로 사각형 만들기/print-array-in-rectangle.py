arr = [[1 for _ in range(5)] for _ in range(5)]

for row in range(1, 5):
    for col in range(1, 5):
        arr[row][col] = arr[row-1][col] + arr[row][col-1]

for i in range(5):
    print(*arr[i])