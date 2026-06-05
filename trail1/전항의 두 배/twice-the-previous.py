fir, sec = map(int, input().split())

arr = [fir, sec]

for i in range(3, 11):
    arr.append(arr[-1] + arr[-2]*2)

print(*arr, end='')